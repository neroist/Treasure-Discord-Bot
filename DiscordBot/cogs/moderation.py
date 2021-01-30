import asyncio
import discord
import math 
import json
from discord.ext import commands

space = ' '
checkmark = ":white_check_mark:"

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| bans given user')
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

    @commands.has_permissions(kick_members=True)
    @commands.command(help='| Removes given user from the server')
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
    async def clear(self, ctx, amount=1, member: discord.Member = None):
        if member != None:
            await ctx.channel.purge(limit=amount, check=lambda msg: msg.author == member)
        else:
            await ctx.channel.purge(limit=amount)

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
    @commands.command(help='| Temporarily bans a member. Put quotes around the time you want to ban the person.')
    async def tempban(self, ctx, member: discord.Member, time: str, reason):
        time = time.split(' ')

        for tim in time:
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
            title='Temp-Ban',
            description=f'{ctx.message.author} has banned {member.name}!',
            color=discord.Colour.dark_red()
        )

        ban_embed.add_field(name='Reason: ', value=reason, inline=True)
        ban_embed.add_field(name='Time: ', value=time)

        await ctx.send(embed=ban_embed)

        await member.ban()
        await asyncio.sleep(time)
        await member.unban()

    @commands.has_permissions(manage_messages=True)
    @commands.command(help='| Blacklists words from being said')
    async def blacklist(self, ctx, *words):
        words = list(words)

        with open('cogs/blacklisted.json', 'r+') as file:
            blacklisted = json.load(file)
            blacklisted[str(ctx.guild.id)] = []
            wierd = blacklisted[str(ctx.guild.id)]

            wierd.extend(words)
            json.dump(blacklisted, file, indent=4)
            file.close()

        ctx.send(f'{checkmark}\nWords: {words} were successfully blacklisted.\nWill update in aprox. 5 minutes')
        


def setup(client):
    client.add_cog(Moderation(client))
