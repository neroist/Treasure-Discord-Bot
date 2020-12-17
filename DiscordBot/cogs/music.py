import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.has_permissions(speak=True, connect=True)
    @commands.command(aliases=['p', 'play', 'playmusic'], help='| plays a song in the voice channel you are in')
    async def music_play(self, ctx, song):
        ctx.send('Command coming soon!')

    @commands.has_permissions(speak=True, connect=True)
    @commands.command(help='| makes the bot join the voice channel you are in')
    async def join(self, ctx):
        ctx.send('Command comming soon!')

    @commands.has_permissions(speak=True, connect=True)
    @commands.command(help='| makes the bot leave the voice channel it is in')
    async def leave(self, ctx):
        ctx.send('Command comming soon!')


def setup(client):
    client.add_cog(Music(client))
