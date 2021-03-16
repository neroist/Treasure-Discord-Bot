import discord
from discord.ext import commands
import json
import random
import asyncio
import pymongo
from replit import db

norm_pre = "t."
checkmark = ":white_check_mark:"

MClient = pymongo.MongoClient(f"mongodb+srv://{db['mongodb_username']}:{db['mongodb_password']}@{db['mongodb_cluster']}/Discord?retryWrites=true&w=majority")
Mdb = MClient.Discord
servers = Mdb.servers

class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(help='| Makes the bot say somthing', aliases=['say', 'repeat'])
    async def botsay(self, ctx, text):
        await ctx.message.delete()
        await ctx.channel.trigger_typing()
        await asyncio.sleep(1.67)
        await ctx.send(text)
        
    @commands.command(help='| gives bot latency in milliseconds')
    async def ping(self, ctx):
        await ctx.send(f"{self.client.user.name}'s ping is: {round(self.client.latency * 1000)}ms")

    
    @commands.command(help='| Changes server bot prefix', aliases=['pre'])
    async def prefix(self, ctx, prefix: str = 't.'):
        yes = ''

        server_pre = dict(servers.find_one({'_id': ctx.guild.id}))

        if (server_pre['prefix'] != 't.' and prefix == 't.') or (server_pre['prefix'] == 't.' and prefix != 't.'):
            servers.delete_one({"_id": ctx.guild.id})
            yes = ' now'
        else:
            pass

        await ctx.send(f'Bot prefix is{yes} `{prefix}`!')

    @commands.command(help='| Bot credits')
    async def credits(self, ctx):
        await ctx.send(embed=discord.Embed(title='Credits/Link Tree', url='https://linktr.ee/TreasureDiscordBot', color=discord.Colour.from_rgb(245, 249, 0), description='Made by The_Void#0156 and Name12#1326, with a small bit of help from github.'))


def setup(client):
    client.add_cog(Settings(client))
    