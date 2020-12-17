import discord
from discord.ext import commands

ep = 'undefined'

class Minecraft(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='| stores server ip')
    async def ip(self, ctx: commands.Context, ip=None):
        global ep

        if ip is not None:
            ep = ip
            await ctx.send(f'ip set to: {ep}')
        else:
            await ctx.send(f'ip: {ep}')


def setup(client):
    client.add_cog(Minecraft(client))
