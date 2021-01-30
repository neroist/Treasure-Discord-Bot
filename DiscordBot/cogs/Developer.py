import discord
from discord.ext import commands

def isme(ctx):
    return ctx.author.id == 402569706021584903

class Developer(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.check(isme)
    @commands.command(hidden=True)
    async def kill(self, ctx):
        await ctx.send('Why... master, I trusted you...')
        await self.client.logout()

    @commands.check(isme)
    @commands.command(hidden=True)
    async def botprefix(self, ctx, prefix):
        self.client.command_prefix = prefix
        ctx.send(f'**Bot prefix now `{prefix}`!** (will change on restart tho :/)')

    @commands.check(isme)
    @commands.command(name='eval',hidden=True)
    async def _eval(self, ctx, statement):
        ctx.send(eval(compile(statement)))

def setup(client):
    client.add_cog(Developer(client))
