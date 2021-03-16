import discord
from discord.ext import commands

import json
from datetime import date
from simpleeval import simple_eval
from string import ascii_letters

pollDesu = """Usage: t.poll <question> <channel>\n\nParameters:\n    <question> - The question that is going into your poll\n   <channel> (optional) - the channel to post the poll into; can only be used by people that have the `Manage Channels` permissition"""



class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='gives info on given user', aliases=['memberinfo'])
    async def whois(self, ctx, member: discord.Member):
        if member.is_on_mobile():
            device = 'Mobile'
        else:
            device = 'Computer'

        activity = member.activity
        act_add = ''

        if activity.type == discord.ActivityType.playing:
            act_add = 'playing '
        elif activity.type == discord.ActivityType.listening:
            act_add = 'listening to '
        elif activity.type == discord.ActivityType.watching:
            act_add = 'watching '
        elif activity.type == discord.ActivityType.competing:
            act_add = 'competing in '
        elif activity.type == discord.ActivityType.streaming:
            act_add = 'streaming '

        activity = act_add + activity.name

        now = str(date.today())
        rroles = []

        for i in member.roles[1:]:
            rroles.append(i.mention)

        #reverses the roles list, and casts it into a string 
        roles = str(rroles[::-1])[1:-1]
        roles = roles.replace("'", '')


        embed = discord.Embed(title="User Info", color=member.colour)
        embed.add_field(name="Name:", value=member.name, inline=True)
        embed.add_field(name="Joined:", value=member.joined_at.strftime('%A, %B %d, %Y %I:%M %p'), inline=True)
        embed.add_field(name='Created:', value=member.created_at.strftime('%A, %B %d, %Y %I:%M %p'), inline=True)
        embed.add_field(name='Status:', value=member.raw_status, inline=True)
        embed.add_field(name="Activity:", value=activity, inline=True)
        embed.add_field(name="Device:", value=device, inline=True)
        embed.add_field(name='Bot:', value=member.bot, inline=True)
        embed.add_field(name="Color:", value=member.colour, inline=True)
        embed.add_field(name='Roles:', value=roles, inline=True)
        embed.add_field(name='Top Role', value=rroles[-1], inline=True)
        embed.add_field(name='Permissions:', value=member.guild_permissions, inline=True)
        embed.add_field(name='Id:', value=member.id, inline=True)
        embed.set_footer(text=f"Treasure • {now}")
        
        embed.set_thumbnail(url=str(member.avatar_url))

        await ctx.send(embed=embed)

    @commands.command(help='Gives info on the server', aliases=['si', 'serveri', 'servinfo', 'sinfo'])
    async def serverinfo(self, ctx):
        #ctx.send('coming soon :)')
        guild = ctx.guild
        now = str(date.today())
        channels = list()
        bots = list()
        subs = list()

        for (i, x) in zip(guild.text_channels, guild.voice_channels):
            channels.append(i.name)
            channels.append(x.name)

        for i in guild.premium_subscribers:
            subs.append(i.mention)

        for i in guild.members:
            if i.bot:
                bots.append(str(i.mention))

        subs = str(subs)[1:-1]
        subs = subs.replace("'", '')

        if subs == '':
            subs = None

        bots = str(bots)[1:-1]
        bots = bots.replace("'", '')

        info_names = iter([
            "Name:", 
            "Created at:", 
            'Owner:', 
            "Guild Boosters:", 
            'Bots:', 
            "Highest Role:", 
            'Member Count:', 
            'Rules Channel:', 
            'Id:'
        ])

        namecp = [
            "Name:", 
            "Created at:", 
            'Owner:', 
            "Guild Boosters:", 
            'Bots:', 
            "Highest Role:", 
            'Member Count:', 
            'Rules Channel:', 
            'Id:'
        ]

        info_values = iter([
            guild.name, 
            guild.created_at.strftime('%A, %B %d, %Y %I:%M %p'), 
            str(guild.owner), 
            subs, 
            bots, 
            guild.roles[-1].mention, 
            guild.member_count, 
            guild.rules_channel.mention, 
            guild.id
        ])

        embed = discord.Embed(title="Server Info", color=discord.Colour.purple())

        for _ in range(len(namecp)):   
            embed.add_field(name=next(info_names), value=next(info_values), inline=True)

        embed.set_thumbnail(url=str(guild.icon_url))

        embed.set_footer(text=f"Treasure • {now}")
        await ctx.send(embed=embed)


    @commands.command(help='Solves math equasion')
    async def math(self, ctx, eqa: str):
        for it in eqa:
            if it in ascii_letters:
                await ctx.send('bruh no letters ik what ur tryna do')
                return

        eqa.replace('^', '**')
        await ctx.send(eval(eqa))


    @commands.command(name='poll', description=pollDesu)
    async def _poll(self, ctx, *, question: str, channel = None):
        """Creates a poll inside a discord embed"""

        if question.lower()[-1] != "?":
                question = f"{question}?"

        embed = discord.Embed(title=f'Poll by {str(ctx.author)}', description=question, color=ctx.author.color())
        sent = await ctx.send(embed=embed)

        await sent.add_reaction('✅')
        await sent.add_reaction('❌')


def setup(client):
    client.add_cog(General(client))
