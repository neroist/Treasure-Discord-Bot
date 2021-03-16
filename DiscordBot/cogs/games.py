import discord
from discord.ext import commands
import asyncio
import random
from akinator.async_aki import Akinator
import akinator
import os
import json
from random import choice

class Games(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def dicegame(self, ctx):
        """Play a dice game where you and the bot rolls. If the number you rolled is higher than what the bot did, you win and vice versa."""

        embed = discord.Embed(title="Dice game!", description="")
        number1 = random.randint(1,12)
        number2 = random.randint(1,12)
        if number1 > number2:
          title = "You won!"
          end = "Because you rolled more than me, you won."
        elif number1 < number2:
          title = "You lost!"
          end = "Because I rolled more than you, I won."
        else:
          title = "It's a draw!"
          end = "Because I rolled the same as you, it's draw."
        numbers = "You rolled " + str(number1) + " and I rolled " + str(number2) + ". " + end
        embed.add_field(name=title, value=numbers)
        await ctx.send(embed=embed)

    #normal version
    @commands.command()
    async def slot(self, ctx):
        embed = discord.Embed(title="Slot Machhine", description="", colour=discord.Colour.green())
        slots = ("💜", "🧨", "🧧", "🎡", "👑", "💎", "🏆", "📄", "🚲", "🚦", "🍜", "🍃", "💯")
        if os.getenv('rigd')==True:
        	while True:  
        		slot1 = random.choice(slots)
        		slot2 = random.choice(slots)
        		slot3 = random.choice(slots)
        		if slot1==slot2 and slot1==slot3:
        			slot1 = random.choice(slots)
        			slot2 = random.choice(slots)
        			slot3 = random.choice(slots)
        		else:
        			break
        else:
        	slot1 = random.choice(slots)
        	slot2 = random.choice(slots)
        	slot3 = random.choice(slots)
        des = "Your three slots are: " + slot1 + ", " + slot2 + " and " + slot3 + "."
        if slot1 == slot2 == slot3:
        	title = "All of the slots were the same!!! Jackpot!!!"
        elif slot1 == slot2:
        	title = "Two of the slots were the same!! Very lucky!!"
        elif slot2 == slot3:
        	title = "Two of the slots were the same!! Very lucky!!"
        elif slot1 == slot3:
        	title = "Two of the slots were the same!! Very lucky!!"
        else:
        	title = "None of the slots were the same! Better luck next time!"
        embed.add_field(name=title, value=des)
        await ctx.send(embed=embed)

    @commands.command()
    async def roulette(self, ctx, number):
        numberr = random.randint(0,50)
        if numberr == int(number):
            title = "You won!"
        else:
            title = "You lost!"
        des = "The ball landed on " + str(numberr) + " and your number was " + str(number)
        embed = discord.Embed(title="Roulette", description="")
        embed.add_field(name=title, value=des)
        await ctx.send(embed=embed)

    @commands.command()
    async def lottery(self, ctx, number1, number2, number3, number4, number5):
    	number = 0
    	Number1 = int(number1)
    	Number2 = int(number2)
    	Number3 = int(number3)
    	Number4 = int(number4)  
    	Number5 = int(number5)
    	Rand1 = random.randint(1,50)
    	rand1 = int(Rand1)
    	Rand2 = random.randint(1,50)
    	rand2 = int(Rand2)
    	Rand3 = random.randint(1,50)
    	rand3 = int(Rand3)
    	Rand4 = random.randint(1,50)
    	rand4 = int(Rand4)
    	Rand5 = random.randint(1,50)
    	rand5 = int(Rand5)
    	RandomNumbers = rand1,rand2,rand3,rand4,rand5
    	if Number1 in RandomNumbers:
    		number = number + 1
    	if Number2 in RandomNumbers:
    		number = number + 1
    	if Number3 in RandomNumbers:
    		number = number + 1
    	if Number4 in RandomNumbers:
    		number = number + 1
    	if Number5 in RandomNumbers:
    		number = number + 1
    	title = "You got " + str(number) + " numbers correct!"
    	des="The correct numbers are:",rand1,rand2,rand3,rand4,rand5,
    	embed = discord.Embed(title="Lottery", description="")
    	embed.add_field(name=title, value=des)
    	await ctx.send(embed=embed)

    @commands.command()
    async def rps(self, ctx, player):
        play = player.capitalize() 
        all = ["paper", "rock","scissors"]
        com = random.choice(all)
        com2 = com.capitalize() 
        if com2 == "Rock" and play == "Paper":
            title = "You won!"
        elif com2 == "Paper" and play == "Paper":
            title = "It's a draw!"
        elif com2 == "Scissors" and play == "Paper":
            title = "You lost!"
        elif com2 == "Rock" and play == "Rock":
            title = "It's a draw!"
        elif com2 == "Paper" and play == "Rock":
            title = "You lost!"
        elif com2 == "Scissors" and play == "Rock":
            title = "You won!"
        elif com2 == "Rock" and play == "Scissors":
            title = "You lost!"
        elif com2 == "Paper" and play == "Scissors":
            title = "You won!"
        elif com2 == "Scissors" and play == "Scissors":
            title = "It's a draw!"
        else:
            title = "That is not a valid option"
        des = "You chose " + play + ", and the bot chose " + com2 + "."
        embed = discord.Embed(title="Rock Paper Scissors", description="")
        embed.add_field(name=title, value=des)
        await ctx.send(embed=embed)

    @commands.command(help='| Akinator, tries to guess whoever you are thinking about', name='akinator')
    async def _akinator(self, ctx, language='en'):
        aki = Akinator()
        nsfw = ctx.channel.is_nsfw()
        valid = ['✅', '❌', '🔙', '🤷‍♀️']

        def check(reaction, user):
            return str(reaction.emoji) in valid and user == ctx.message.author

        async def main():
            q = await aki.start_game(language=language, child_mode=nsfw)

            embed = discord.Embed(title="Akinator Asks", description=q)
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
        #if this doesnt work try loop.run_until_complete(man) or loop.run_until_complete(await man())
        loop.run_until_complete(main())
        loop.close()

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

def setup(bot):
    bot.add_cog(Games(bot))
    