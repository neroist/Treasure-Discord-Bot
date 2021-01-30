import discord
from discord.ext import commands
import json

norm_pre = "t."
checkmark = ":white_check_mark:"

class Treasure(commands.Cog, name='Bot'):
    def __init__(self, client):
        self.client = client
    
    @commands.command(help='| Makes the bot say somthing', aliases=['say', 'repeat'])
    async def botsay(self, ctx, text):
        await ctx.send(text)
        await ctx.message.delete()

    @commands.command(help='| gives bot latency in milliseconds')
    async def ping(self, ctx):
        await ctx.send(f"{self.client.user.name}'s ping is: {round(self.client.latency * 1000)}ms")

    
    @commands.command(help='| Changes server bot prefix')
    async def prefix(self, ctx, prefix: str, aliases=['pre']):
        yes = ''

        if yes=='':
            with open('DiscordBot/prefixes.json', 'r+') as file:
                dit = json.load(file)
                dit[str(ctx.guild.id)] = prefix
                file.seek(0)

                json.dump(dit, file, indent=4)
                file.close()
            yes = ' now '

        await ctx.send(f'Bot prefix is{yes}`{prefix}`!')


def setup(client):
    client.add_cog(Treasure(client))