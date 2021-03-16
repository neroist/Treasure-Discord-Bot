from datetime import date
import discord
import json
from discord.ext import commands
from inspect import signature
from discord import Colour

class Help(commands.Cog):
    """All help commands"""

    def __init__(self, client):
        self.client = client

    def get_cog_help(self, cog, color=Colour.random()):
        ccog = str(cog)
        cog = self.client.get_cog(ccog)

        embed = discord.Embed(title=f"{ccog.title()} commands", description=cog.description, color=color)

        for i in cog.get_commands():
            embed.add_field(name=f't.{i.name}', value=str(i.help)[2:])
        
        now = str(date.today())
        embed.set_footer(text=f"Treasure • {now}")

        return embed

    def filter_param_type_hints(func):
        params = signature(func)
        params_str = str(params)[1:-1]

        list_to_filter = ["str", 'int', 'set', 'discord.Member', '*,', 'list', 'tuple', '*', '=', 'None', 'self', 'ctx', ':']

        for y in list_to_filter:
            params_str.replace(y, '')

        return params_str

    @commands.command(help='Shows the help message')
    async def help(self, ctx, command=None):

        if command == None:
            embed = discord.Embed(title="help", description="Thanks for using this bot! \n\nBot created by Name12#1326 and The_Void#0156\n\n Do \"t.help <command>\" for more information on a command!\n" , color=discord.Color.from_rgb(229, 234, 19))
            for cog in self.client.cogs:

                if cog.lower() == 'developer':
                    pass
                else:
                    embed.add_field(name=f't.{cog.lower()}', value=f'See the {cog} commands')

            now = str(date.today())
            embed.set_footer(text=f"Treasure • {now}")

            await ctx.send(embed=embed)
        else:
            command = self.client.get_command(command)

            if command == None:
                await ctx.send('Command not found')
                return
            else:
                now = str(date.today())
                
                embed = discord.Embed(title=f't.{command.name}', description=command.description, color=Colour.random())
                embed.set_footer(text=f"Treasure • {now}")
                embed.add_field(name="Description:", value=command.help)
                embed.add_field(name="Parameters:", value=eval('filter_param_type_hints()'))
                

                await ctx.send(embed=embed)


    @commands.command(help='General commands')
    async def general(self, ctx):
        embed = self.get_cog_help("General", Colour.from_rgb(28, 226, 44))
        await ctx.send(embed=embed)

    @commands.command(help='Moderation commands')
    async def moderation(self, ctx):
        embed = self.get_cog_help("Moderation", Colour.from_rgb(238, 80, 83))
        await ctx.send(embed=embed)

    @commands.command(help='go to the game page')
    async def games(self, ctx):
        embed = self.get_cog_help("Games", Colour.from_rgb(28, 226, 44))
        await ctx.send(embed=embed)

    @commands.command()
    async def music(self, ctx):
        embed = self.get_cog_help("Music", Colour.from_rgb(135, 36, 235))
        await ctx.send(embed=embed)

    @commands.command()
    async def settings(self, ctx):
        embed = self.get_cog_help("Settings", Colour.from_rgb(117, 117, 117))
        await ctx.send(embed=embed)

    @commands.command()
    async def fun(self, ctx):
        embed = self.get_cog_help("Fun", Colour.from_rgb(249, 155, 45))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))