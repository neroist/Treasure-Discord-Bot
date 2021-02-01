import discord
from discord.ext import commands
import json

norm_pre = "t."
checkmark = ":white_check_mark:"

class Settings(commands.Cog, name='Bot'):
    def __init__(self, client):
        self.client = client
    
    @commands.command(help='| Makes the bot say somthing', aliases=['say', 'repeat'])
    async def botsay(self, ctx, text):
        await ctx.message.delete()
        await ctx.send(text)
        
    @commands.command(help='| gives bot latency in milliseconds')
    async def ping(self, ctx):
        await ctx.send(f"{self.client.user.name}'s ping is: {round(self.client.latency * 1000)}ms")

    
    @commands.command(help='| Changes server bot prefix', aliases=['pre'])
    async def prefix(self, ctx, prefix: str = 't.'):
        yes = ''

        with open('DiscordBot/prefixes.json') as file:
            server_pre = json.load(file)
            file.close()

        if (server_pre[str(ctx.guild.id)] != 't.' and prefix == 't.') or (server_pre[str(ctx.guild.id)] == 't.' and prefix != 't.'):
            with open('DiscordBot/prefixes.json', 'w') as file:
                server_pre[str(ctx.guild.id)] = prefix
                json.dump(server_pre, file, indent=4)
                file.close()

            yes = ' now'
        else:
            pass
        await ctx.send(f'Bot prefix is{yes} `{prefix}`!')

    @commands.command(help='| Bot credits')
    async def credits(self, ctx):
        await ctx.send(embed=discord.Embed(description='Made by The_Void#0156 and Name12#1326, with a small bit of help from github.'))


def setup(client):
    client.add_cog(Settings(client))
    