from datetime import date
import discord
import json
from discord.ext import commands
from simpleeval import simple_eval
from string import ascii_letters

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(change_nickname=True, manage_nicknames=True)
    @commands.command(help='| Changes a users nickname', aliases=['nickname', 'change_nickname', 'changenick', 'chn'])
    async def nick(self, ctx, member: discord.Member, *, nickname):
        await member.edit(nick=nickname)
        await ctx.send(
            f'Nickname was successfully changed for {member.mention} to {nickname}.'
        )

    @commands.command(help='| gives info on given user', aliases=['wi', 'whoi', 'wis', 'memberinfo'])
    async def whois(self, ctx, member: discord.Member):
        if member.is_on_mobile:
            device = 'Mobile'
        else:
            device = 'Computer'

        now = str(date.today())
        roles = ' '.join(member.roles[:-1])

        embed = discord.Embed(title="User Info", color=discord.Colour.purple())
        embed.add_field(name="Name:", value=member.name, inline=True)
        embed.add_field(name="Joined Guild:", value=member.joined_at, inline=True)
        embed.add_field(name='Discord Staff:', value=member.system, inline=True)
        embed.add_field(name='Status:', value=member.raw_status, inline=True)
        embed.add_field(name="Activity:", value=member.activity, inline=True)
        embed.add_field(name="Device:", value=device, inline=True)
        embed.add_field(name='Bot:', value=member.bot, inline=True)
        embed.add_field(name="Color:", value=member.colour, inline=True)
        embed.add_field(name='Roles:', value=roles, inline=True)
        embed.add_field(name='Top Role', value=member.top_role, inline=True)
        embed.add_field(name='Permissions:', value=member.guild_permissions, inline=True)
        embed.add_field(name='Id:', value=member.id, inline=True)

        embed.set_footer(text=f"Treasure • {now}")
        await ctx.send(embed=embed)

    @commands.command(help='| Gives info on the server')
    async def serverinfo(self, ctx, aliases=['si', 'serveri', 'servinfo', 'sinfo']):
        #ctx.send('coming soon :)')
        guild = ctx.guild
        now = str(date.today())
        channels = list()
        bots = list()

        for i, x in guild.text_channels, guild.voice_channels:
            channels.append(i.name)
            channels.append(x.name)

        for i in guild.members:
            if i.bot:
                bots.append(str(i))

        embed = discord.Embed(title="Server Info", color=discord.Colour.purple())
        embed.add_field(name="Name:", value=guild.name, inline=True)
        embed.add_field(name="Created at:", value=guild.created_at, inline=True)
        embed.add_field(name='Owner:', value=guild.owner, inline=True)
        embed.add_field(name='Owner Id:', value=guild.owner_id, inline=True)
        embed.add_field(name='Channels:', value=channels, inline=True)
        embed.add_field(name="Guild Boosters:", value=guild.premium_subcribers, inline=True)
        embed.add_field(name='Bots:', value=bots, inline=True)
        embed.add_field(name="Highest Role:", value=guild.roles[-1], inline=True)
        embed.add_field(name='Roles:', value=guild.roles[::-1], inline=True)
        embed.add_field(name='Member Count:', value=guild.member_count, inline=True)
        embed.add_field(name='Rules Channel:', value=guild.rules_channel, inline=True)
        embed.add_field(name='Id:', value=guild.id, inline=True)

        embed.set_footer(text=f"Treasure • {now}")
        await ctx.send(embed=embed)


    @commands.command()
    async def math(self, ctx, eqa: str):
        for it in eqa:
            if it in ascii_letters:
                ctx.send('bruh no letters ik what ur tryna do')
                return

        eqa.replace('^', '**')
        ctx.send(simple_eval(eqa))


def setup(client):
    client.add_cog(General(client))
