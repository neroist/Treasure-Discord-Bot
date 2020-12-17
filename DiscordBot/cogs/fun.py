import discord
from discord.ext import commands
from random import *

space = ' '

class Fun(commands.Cog):
    def __init__(self, Client):
        self.client = Client
        
    @commands.has_permissions(send_messages=True)
    @commands.command(name='8ball', help='| 8ball in discord, ask it a question')
    async def _8ball(self, ctx, *, question):
        author = ctx.message.author
        pfp = author.avatar_url
        phrases = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]  
        ibetit = discord.Embed(
            title='8-Ball',
            colour=discord.Colour.blue()
            )
        
        ibetit.add_field(name='Question: ', value=question, inline=False)
        ibetit.set_author(name=author, icon_url=pfp)
        ibetit.add_field(name='Answer: ', value=choice(phrases), inline=False)
        
        await ctx.send(embed=ibetit)

    @commands.has_permissions(manage_messages=True)
    @commands.command(name='spam', help='| Spams a certain message however many times you want, you can choose if you want TTS(Talk-To-Speech) aswell. And make sure to put quotes on what you want to spam')
    async def spam_messages(self, ctx, message, iterby:int, TTS=False):
        if message.startswith('.'):
            await ctx.send('You can\'t spam commands! >:(' ) 
            return

        if str(ctx.message.author) != 'The_Void#0156':
            await ctx.send('This command is only available to the creator of the bot currently.')
            return
            
        if iterby >= 100:
            await ctx.send('i can\'t send that many messages.')
            return

        await ctx.message.delete()
        for i in range(iterby):
            await ctx.channel.send(message)

    @commands.has_permissions(send_messages=True)
    @commands.command(help='| tells a yo mama joke')
    async def yomama(self, ctx):
        yo_mama_jokes = [
            'Yo mama so ugly even Hello Kitty said good bye.',
            'Yo mama so skinny when she swallowed a meatball everyone thought she was pregnant again.',
            'Yo mama so ugly when she looks in the mirror her reflection ducks.',
            "Yo mama so stupid she tried to put her M&Ms in alphabetical order.",
            'Yo mama so stupid she went to the dentist to get a blue tooth.',
            'Yo mama so stupid she got locked in a mattress store and slept on the floor.', 
            'Yo mama so stupid she failed a survey.',
            'Yo mama so stupid she got fired from a blow job.',
            'Yo mama so stupid she thinks Taco Bell is a Mexican phone company. ',
            'Yo mama so stupid she tried to climb Mountain Dew.',
            'Yo mama so stupid she went to the YMCA thinking it\'s Macy\'s.' ,
            'Yo mama is so stupid, she won\'t play Candy Crush cause she has diabetes.',
            'Yo mama so old the back of her head looks like a raisin. ',
            'Yo mama so old her social security number is 1. ',
            'Yo mama so old when she was a child rainbows were still in black and white. ',
            'Yo mama so old when she was in school there was no history class. ',
            'Yo mama so old she has a picture of Moses in her yearbook.',
            'Yo mama so old she was a crossing guard when Moses parted the red sea. ',
            'Yo mama so old she was a waitress at the Last Supper.' ,
            'Yo mama so old she has an autographed bible. ',
            'Yo mama so old she knew Mr. Clean when he had an afro.',
            'Yo mama so old she knew Gandalf before he had a beard.',
            'Yo mama so fat she wears a sock on each toe. ',
            'Yo mama so fat her belly button got an echo. ',
            'Yo mama so fat you have to roll over twice to get off her. ',
            'Yo mama so fat when she takes a bath there\'s no room left for any water in the tub. ',
            'Yo mama so fat when I pictured her in my head I almost broke my neck. ',
            'Yo mama so fat her blood type is Nutella. Yo mama so fat she gave Dracula high cholesterol.' ,
            'Yo mama so fat her ass has its own zip code.',
            'Yo mama so fat she uses bacon as breath mints.',
            'Yo mama so fat she uses Google Earth to take a selfie.',
            'Yo mama so skinny she hula hoops with a cheerio.',
            'Yo mama so skinny she can grate cheese on her ribs. ',
            'Yo mama so skinny her nipples touch. ',
            'Yo mama is so skinny she can dodge raindrops. ',
            'Yo mama\'s so skinny when her pimp slapped her he got a paper cut. ',
            'Yo mama so skinny she uses Chapstick for deodorant.' ,
            'Yo mama so skinny she uses a tea bag as her pillow. ',
            'Yo mama so skinny she uses a Band-Aid as a maxi-pad.' ,
            'Yo mama so skinny when she swallowed a meatball everyone thought she was pregnant again.',
            'Yo mama so skinny if she had a yeast infection she\'d be a Quarter Pounder with cheese.',
            'Yo mama so poor she went to McDonald\'s and put a milkshake on layaway.',
            'Yo mama so poor she has the ducks throw bread at her.',
            'Yo mama so fat she uses Google Earth to take a selfie.',
            'Yo mama so skinny she hula hoops with a cheerio.',
            'Yo mama so hairy people think she\'s an Ewok.',
            'Yo mama so poor when I saw her kicking a can down the street, I asked her what she was doing, she said "Moving.”'
            ]

        await ctx.send(choice(yo_mama_jokes))

def setup(client):
    client.add_cog(Fun(client))
