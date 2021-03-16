import discord
from discord.ext import commands
from replit import clear
import sys
import os

devs = [402569706021584903, 732012983068393583] 

isdev = lambda ctx: ctx.author.id in devs

class Developer(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.check(isdev)
    @commands.command(hidden=True)
    async def kill(self, ctx):
        await ctx.send('Why... master, I trusted you...')
        await self.client.logout()

    @commands.check(isdev)
    @commands.command(hidden=True)
    async def botprefix(self, ctx, prefix):
        self.client.command_prefix = prefix
        await ctx.send(f'**Bot prefix now `{prefix}`!** (will change on restart tho :/)')

    @commands.check(isdev)
    @commands.command(aliases=["r"], hidden=True)
    async def restart(ctx):  
        clear()
        os.execv(sys.executable, ['python',] + sys.argv)

        embed=discord.Embed(title=":white_check_mark:", description="Successfully Restarted")
        await ctx.send(embed=embed)

        print("succesfully restarted")

    @commands.check(isdev)
    @commands.command(hidden=True)
    async def status(self, ctx, status: str):
        game = discord.Game(status)

        await self.client.change_presence(activity=game, status=discord.Status.online(), afk=True)

def setup(client):
    client.add_cog(Developer(client))
