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
        
    @commands.command(name='8ball', help='| 8ball in discord, ask it a question', aliases=['8b'])
    async def _8ball(self, ctx, *, question):
        author = ctx.message.author
        pfp = author.avatar_url

        with open('DiscordBot/cogs/8_ball_phrases.json') as file:
            phrases = json.load(file)
            file.close()


        intuit = discord.Embed(
            title='8-Ball',
            colour=discord.Colour.blue()
            )
        
        intuit.add_field(name='Question: ', value=question, inline=True)
        intuit.set_author(name=author, icon_url=pfp)
        intuit.add_field(name='Answer: ', value=choice(phrases), inline=True)
        intuit.set_thumbnail(url='https://magic-8ball.com/assets/images/magicBallStart.webp')

        await ctx.send(embed=intuit)

    @commands.command(help='| tells a yo mama joke')
    async def yomama(self, ctx):
        with open('DiscordBot/cogs/yo_mama.json') as jokes:
            yo_mama_jokes = json.load(jokes)
            jokes.close()

        await ctx.send(choice(yo_mama_jokes))

    @commands.command(help='| Akinator', name='akinator')
    async def _akinator(self, ctx, language='en'):
        aki = Akinator()
        nsfw = ctx.channel.is_nsfw()
        valid = ['✅', '❌', '🔙', '🤷‍♀️']

        def check(reaction, user):
            return str(reaction.emoji) in valid and user == ctx.message.author

        async def man():
            q = await aki.start_game(language=language, child_mode=nsfw)
    
            embed = discord.Embed(title="\r\u200b", description=q)
            mess = await ctx.send(embed=embed)
            await mess.add_reaction('✅')
            await mess.add_reaction('❌')
            await mess.add_reaction('🔙')
            await mess.add_reaction('🤷‍♀️')

            while aki.progression <= 80:
                reaction, user = await self.client.wait_for('reaction_add', timeout=120, check=check)
                try:
                    if str(reaction.emoji) == '🔙':
                        try:
                            q = await aki.back()
                        except akinator.CantGoBackAnyFurther:
                            pass
                    elif str(reaction.emoji) == '❌':
                        q = 'yes'
                    elif str(reaction.emoji) == '✅':
                        q = 'no'
                    elif str(reaction.emoji) == '🤷‍♀️':
                        q = 'idk'
                except Exception as e:
                    ctx.send(e)
                finally:
                    qe = await aki.answer(q)
                    embed = discord.Embed(title='\r\u200b', description=qe)

                    mess = await ctx.send(embed=embed)
                    await mess.add_reaction('✅')
                    await mess.add_reaction('❌')
                    await mess.add_reaction('🔙')
                    await mess.add_reaction('🤷‍♀️')

                    
            await aki.win()

            first_guess = dict(aki.first_guess)
            embed = discord.Embed(title=f"It's {first_guess['name']} ({first_guess['description']}!) Was I correct?", image=first_guess['absolute_picture_path'])
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('✅')
            await msg.add_reaction('❌')

            try:
                correct, user = await self.client.wait_for('reaction_add', timeout=120, check=check)
            except asyncio.TimeoutError:
                pass
            
            if str(correct.emoji) == "✅":
                await ctx.send("Yay\n")
            else:
                await ctx.send("Oof\n")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(man)
        loop.close()

    @commands.command(help='| Gives you some DANK memes from reddit')
    async def meme(self, ctx, limit=1):
        for submission in range(limit):
            submission = reddit.subreddit(choice(['dankmemes', 'memes'])).random_rising()
            embed = discord.Embed(title=submission.title, url=f'https://www.reddit.com{submission.permalink}')
            embed.set_image(url=submission.url)

            await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Fun(client))
