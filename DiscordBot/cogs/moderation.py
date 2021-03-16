import asyncio
import discord
import math 
import json
from discord.ext import commands
import re

space = ' '
checkmark = ":white_check_mark:"
is_nuking = False

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(help='| Changes a users nickname', aliases=['nickname', 'change_nickname', 'changenick', 'chn'])
    async def nick(self, ctx, member: discord.Member, *, nickname):
        await member.edit(nick=nickname)
        await ctx.send(
            f'Nickname was successfully changed for {member.mention} to {nickname}.'
        )

    @commands.command(help='| bans given user')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):

        if member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
    
        await member.ban()

        ended = discord.Embed(
            title=f'{ctx.message.author.name} has banned {member}',
            colour=discord.Colour.red(),
            description=f'{member} has been banned by {ctx.message.author.name}!'
        )
        ended.add_field(name='Reason:', value=reason)
        await ctx.channel.send(embed=ended)

        inked = discord.Embed(
            title=f'You have been banned from{member.guild.name}!',
            description=f'You have been banned for {reason}',
            colour=discord.Colour.red()
        )
        await member.send(embed=inked)

    @commands.command(help='| bans given users')
    @commands.has_permissions(ban_members=True)
    async def prune(self, ctx, reason, *members):
        if ctx.author in members:
            await ctx.send("You cannot ban yourself")
            return

        if members == () or members == tuple():
            await ctx.send('no list of members to ban given')
            return

        async for member in members:
            if type(member) != discord.Member:
                await ctx.send("")
                

        for member in members:
            try:
                await member.ban()
            except discord.Forbidden:
                await ctx.send(f" Unfortunately, {member.mention} cannot be banned by me. Insuffient permissions")
            
            try:
                inked = discord.Embed(
                        title=f'You have been banned from{member.guild.name}!',
                        description=f'You have been banned for {reason}',
                        colour=discord.Colour.dark_red()
                    )
                await member.send(embed=inked)
            except discord.Forbidden:
                await ctx.send(f'Cannot send {member} embed DM')
            


        ended = discord.Embed(
            title=f'{ctx.message.author.name} has banned {member}',
            colour=discord.Colour.red(),
            description=f'{members} has been banned by {ctx.message.author.name}!'
        )
        ended.add_field(name='Reason:', value=reason)
        await ctx.channel.send(embed=ended)

    @commands.command(help='| Removes given user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        if member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself")
            return

        await member.kick()
        ended = discord.Embed(
            title=f'{ctx.message.author.mention} has kicked {member.mention}',
            description=f'{member} has been kicked!\n**Reason:**{reason}',
            colour=discord.Colour.red()
        )
        await ctx.channel.send(embed=ended)

    @commands.has_permissions(manage_messages=True)
    @commands.command(help='| deletes an amount of messages, default is 1')
    async def clear(self, ctx, amount=0, member: discord.Member = None):
        if member != None:
            await ctx.channel.purge(limit=amount+1, check=lambda msg: msg.author == member)
        else:
            await ctx.channel.purge(limit=amount+1)

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| unbans given user')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f"Unbanned: {str(user)}")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def tempban(self, ctx, member: discord.Member, reason, *time: str):
        """Temporarily bans a member. Put quotes around the time you want to ban the person.
        
        Time codes: 

            s: seconds
            m: minutes
            h: hours
            d: days
            w: weeks
        """
        

        for x, tim in enumerate(time):
            if tim[-1] == 'h':
                time = int(tim[:-1]) * 3600
            elif tim[-1] == 'm':
                time = int(tim[:-1]) * 60
            elif tim[-1] == 'd':
                time = int(tim[:-1]) * 86400
            elif tim[-1] == 'w':
                time = int(tim[:-1]) * 604800
            elif tim[-1] == 's':
                time = int(tim[:-1])

        ban_embed = discord.Embed(
            title='Temp Ban',
            description=f'{ctx.message.author} has banned {member.name}!',
            color=0x992d22
        )

        ban_embed.add_field(name='Reason: ', value=reason, inline=True)
        ban_embed.add_field(name='Time: ', value=time, inline=True)

        await ctx.send(embed=ban_embed)

        await member.ban()
        await asyncio.sleep(time)
        await member.unban()

    @commands.has_permissions(manage_messages=True)
    @commands.command(help='| Blacklists words from being said')
    async def blacklist(self, ctx, *words):
        words = list(words)

        with open('cogs/blacklisted.json') as file:
            blacklisted = json.load(file)
            file.close()
        with open('cogs/blacklisted.json', 'w') as file:
            blacklisted[str(ctx.guild.id)] = []
            wierd = blacklisted[str(ctx.guild.id)]

            wierd.extend(words)
            json.dump(blacklisted, file, indent=4)
            file.close()

        embed = discord.Embed(title=checkmark, description=f'Words: {words} were successfully blacklisted.\nWill update in aprox. 5 minutes')

        ctx.send(embed=embed)

    @commands.command(help='| deletes ALL messages from the channel you\'re in')
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx, channel=None):
        global is_nuking

        if is_nuking:
            await ctx.send('busy rn cant do it')
            return

        if channel == None:
            channel = ctx.channel

        valid = ['yes', 'y', 'no', 'n']

        check = lambda message: message.author == ctx.message.author and message.content.lower() in valid

        await ctx.send('Are you sure? (Y/N)')
        mess = await self.client.wait_for('message', timeout=60, check=check)
        cont=mess.content.lower()

        if cont == valid[0] or cont == valid[1]:
            await ctx.send('BLOOD FOR THE BLOOD GOD')

            async for _message in channel.history(limit=None):
                if _message.author == self.client.user and _message.content == 'BLOOD FOR THE BLOOD GOD':
                    pass
                else:
                    await _message.delete()
            
        elif cont == valid[2] or cont == valid[3]:
            await ctx.send('Nuke aborted.')
            return
        else:
            await ctx.send('Invalid input, aborting nuke.')
            return       

    @commands.command(help='Mutes a user from the current server')
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True, manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        """ Mutes a user from the current server. """
        pass
        
    @commands.command(help='Unmutes a user from the current server.')
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True, manage_messages=True)
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):
        """ Unmutes a user from the current server. """
        pass


def setup(client):
    client.add_cog(Moderation(client))
