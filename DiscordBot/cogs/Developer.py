import discord
from discord.ext import commands
from replit import clear
import sys
import os

devs = [402569706021584903, 732012983068393583] 

def isme(ctx):
    return ctx.author.id in devs

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
    @commands.command(name='eval', hidden=True)
    async def _eval(self, ctx, statement):
        ctx.send(eval(compile(statement)))

    @commands.check(isme)
    @commands.command(aliases=["r"], hidden=True)
    async def restart(ctx):  
        clear()
        os.execv(sys.executable, ['python',] + sys.argv)

        embed=discord.Embed(title=":white_check_mark:", description="Successfully Restarted")
        await ctx.send(embed=embed)

        print("succesfully restarted")

def setup(client):
    client.add_cog(Developer(client))
