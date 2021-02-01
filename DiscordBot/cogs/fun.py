import discord
from discord.ext import commands
from random import choice
import praw
import json
from replit import db
from akinator.async_aki import Akinator
import akinator
import asyncio


space = ' '
reddit = praw.Reddit(client_id=db['reddit_id'], 
    client_secret=db['reddit_secret'], 
    password=db['reddit_password'], 
    username="alt-acc-e", 
    user_agent="webhook for python discord bot (by /u/alt-acc-e)")

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(help='| tells a yo mama joke')
    async def yomama(self, ctx):
        with open('DiscordBot/cogs/yo_mama.json') as jokes:
            yo_mama_jokes = json.load(jokes)
            jokes.close()

        await ctx.send(choice(yo_mama_jokes))

    @commands.command(help='| Gives you some DANK memes from reddit')
    async def meme(self, ctx, limit=1):
        for submission in range(limit):
            submission = reddit.subreddit(choice(['dankmemes', 'memes'])).random_rising()
            embed = discord.Embed(title=submission.title, url=f'https://www.reddit.com{submission.permalink}')
            embed.set_image(url=submission.url)

            await ctx.send(embed=embed)

    @commands.command(help='| Gives you some EPIC dad jokes')
    async def dadjoke(self, ctx):
        with open('cogs/dad_jokes') as f:
            jokes = json.load(f)
            f.close()

        await ctx.send(choice(jokes))
        

def setup(client):
    client.add_cog(Fun(client))
