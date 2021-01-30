import discord
from discord.ext import commands
import asyncio

class Relationships(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ComingSoon(self, ctx):
        ctx.send('Coming Soon!')

def setup(client):
    client.add_cog(Relationships(client))