from datetime import date
import discord
import json
from discord.ext import commands
from simpleeval import simple_eval
from string import ascii_letters

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

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

    @commands.command(help='to summon this command')
    async def help(self, ctx, command=None):

        if command == None:
            embed = discord.Embed(title="**Help**", description="Thanks for using this bot! \n Bot created by Name12#1326 and The_Void#0156\n Do \"*help <command>\" for more information on a command!" , color=0xe74c3c)
            for cog in self.client.cogs:

                if cog.lower() == 'developer':
                    pass
                else:
                    embed.add_field(name=f'*{cog.lower()}', value=f'See the {cog} commands')
            embed.add_field(name='*help', value='to summon this command')

            await ctx.send(embed=embed)
        else:
            command = self.client.get_command(command)

            if command == None:
                await ctx.send('Invalid command')
                return
            else:
                embed = discord.Embed(title=f'*{command.name}', description=command.description)
                await ctx.send(embed=embed)


    @commands.command(help='General commands')
    async def general(self, ctx):
        embed =  discord.Embed(title="**General commands**", description=self.description)
        for i in self.get_commands():
            embed.add_field(name=f'*{i.name}', value=i.help)

        await ctx.send(embed=embed)

    @commands.command(help='Moderation commands')
    async def moderation(self, ctx):
        embed =  discord.Embed(title="**Moderation commands**", description=self.description)
        for i in self.client.get_cog('Moderation').get_commands():
            embed.add_field(name=f'*{i.name}', value=i.help)

    @commands.command(help='go to the game page')
    async def games(self, ctx):
        embed = discord.Embed(title="Games", description="Welcome to game center")
        embed.add_field(name="*dicegame", value="to play a dice game")
        embed.add_field(name="*slot", value="to play a slot machhine")
        embed.add_field(name="*roulette [number here]", value="to play roulette")
        embed.add_field(name="*rps [choice here]", value="to play rock paper scissors")
        embed.add_field(name="*yahtzee", value="to play yahtzee")
        embed.add_field(name="*lottery <number1> <number2> <number3> <number4> <number5>", value="to have a round of a lottery")
        embed.add_field(name='*akinator', value='Akinator, tries to guess whoever you are thinking about')
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
                await ctx.send('bruh no letters ik what ur tryna do')
                return

        eqa.replace('^', '**')
        ctx.send(simple_eval(eqa))

    


def setup(client):
    client.add_cog(General(client))
