import discord
from discord.ext import commands
import json

class Treasure(commands.Cog, name='Bot'):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='botsay', help='| Makes the bot say somthing')
    async def _botsay(self, ctx, text):
        await ctx.send(text)
        await ctx.message.delete()

    @commands.command(name='ping', help='| gives bot latency in milliseconds')
    async def robot_latency(self, ctx):
        await ctx.send(f"{self.client.user.name}'s ping is: {round(self.client.latency * 1000)}ms")


def setup(client):
    client.add_cog(Treasure(client))