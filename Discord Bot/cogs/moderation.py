import asyncio
import math
import discord
from discord.ext import commands

space = ' '


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| Removes given user from the server and blocks the user from joining again')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban()

        ended = discord.Embed(
            title=f'{ctx.message.author.name} has banned {member}',
            colour=discord.Colour.red(),
            description=f'{member} has been banned by {ctx.message.content}!'
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
        await member.kick()
        ended = discord.Embed(
            title=f'{ctx.message.author.mention} has kicked {member.mention}',
            description=f'{member} has been kicked!\n**Reason:**{reason}',
            colour=discord.Colour.red()
        )
        await ctx.channel.send(embed=ended)

    @commands.has_permissions(manage_messages=True)
    @commands.command(help='| deletes an amount of messages, default is 1')
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| unblocks a user that was banned from joining')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f"Unbanned: {user.mention}")

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| Temporarily bans a member.')
    async def tempban(self, ctx: commands.Context, member: discord.Member, reason, time: str):
        valid = 'hdywsm'

        if time[-1] == 'h':
            time = int(time[:-1]) * 3600
        if time[-1] == 'min':
            time = int(time[:-1]) * 60
        if time[-1] == 'd':
            time = int(time[:-1]) * 86400
        if time[-1] == 'y':
            time = int(time[:-1]) * 3.154 * math.e + 7
        if time[-1] == 'w':
            time = int(time) * 604800
        if time[-1] == 's':
            time = int(time)
        if time[-1] == 'm':
            time = int(time[:-1]) * 2.628 * math.e + 6

        for val in valid:
            if val != time[-1]:
                time = int(time)

        await member.ban()
        await asyncio.sleep(time)
        await member.unban()

        ban_embed = discord.Embed(
            title='Temp-Ban',
            description=f'{ctx.message.author} has banned {member.name}!',
            color=discord.Colour.dark_red()
        )

        ban_embed.add_field(name='Reason: ', value=reason, inline=True)
        ban_embed.add_field(name='Time: ', value=time)

        await ctx.send(embed=ban_embed)


def setup(client):
    client.add_cog(Moderation(client))
