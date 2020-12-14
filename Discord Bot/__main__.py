import random
import discord
from discord.ext import commands, tasks
from os import listdir
from itertools import cycle
from datetime import date

creator = 'The_Void#0156'
bot = commands.Bot(command_prefix='.')
space = ' '
statuses = cycle([
    discord.Activity(type=discord.ActivityType.competing, name="A Hypixel Tournament"),
    discord.Activity(type=discord.ActivityType.competing, name="A Box"),
    discord.Activity(type=discord.ActivityType.watching, name="hanime.tv"),
    discord.Activity(type=discord.ActivityType.watching, name="4anime.to"),
    discord.Activity(type=discord.ActivityType.watching, name="9anime.live"),
    discord.Activity(type=discord.ActivityType.watching, name="hentaihaven.xxx"),
    discord.Activity(type=discord.ActivityType.listening, name="MC Virgins"),
    discord.Activity(type=discord.ActivityType.watching, name="Pokimane Fart Compilation 4k HDR Dolby Digital"),
    discord.Activity(type=discord.ActivityType.watching, name="xvideos.com"),
    discord.Game(name="Naruto Storm 4"),
    discord.Game(name=".help"),
    discord.Activity(type=discord.ActivityType.streaming, name="epic memes"),
    discord.Activity(type=discord.ActivityType.listening, name="MC Virgins"),
    discord.Activity(type=discord.ActivityType.listening, name=".help"),
    discord.Activity(type=discord.ActivityType.watching, name="hanime.tv"), 
    discord.Game(name='With your dads pp'),
    discord.Activity(type=discord.ActivityType.playing, name="Undertale"),
    discord.Activity(type=discord.ActivityType.custom, name="Coding"),
    ])

@bot.event
async def on_connect():
    print(f'{bot.user.name} has connected to Discord!')

@tasks.loop(minutes=22)
async def change_status():
    await bot.change_presence(activity=next(statuses))

@bot.event 
async def on_ready():
    change_status.start()
    print(f'Logged in as {bot.user.name}')
    print('Discord server: https://discord.com/channels/740075516165357669/740395650536964116')
    print('Command Prefix: "."')

@bot.event
async def on_message(message):
    message_content = str(message.content)

    if message.author == bot.user:
        return

    if message.author.bot:
        return

    if message_content.isupper() is True and len(message_content) >= 7:
        await message.channel.send('Yo man chill with the caps')
        await message.delete()

    if 'nigger' in message_content:
        await message.delete()
        await message.channel.send('DONT SAY THE N-WORD >:(')

    if '<@!402569706021584903>' in message_content:
        await message.delete()

    await bot.process_commands(message=message)

@bot.event
async def on_message_delete(message):
    author = message.author
    integer = random.randint(1, 100)
    
    now = str(date.today())
    now = now.split('-')
    now = '/'.join(now)

    if integer == 1:
        embededed = discord.Embed(description=f'{message.content}', colour=message.author.colour)
        embededed.set_author(name=author, icon_url=author.avatar_url)
        embededed.set_footer(text=f'Treasure • {now}')

        await message.channel.send(embed=embededed)

@bot.event
async def on_error(event, *args, **kwargs):
    print(f'event: {event}\nargs: {args}\nkwargs: {kwargs}')

@bot.event
async def on_command_error(ctx, error):
    command = ctx.message.content
    
    if command.startswith('.'):
        if isinstance(error, discord.errors.Forbidden):
            await ctx.send('I dont have permission to do this!')
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('You\'re missing a reqiured argument for this command!')
        if isinstance(error, commands.errors.PrivateMessageOnly):
            await ctx.send('This command only works in private messages!')
        if isinstance(error, commands.errors.NoPrivateMessage):
            await ctx.send('bruh why are you trying this command here it doesnt work. jeez i work too much')
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send('That command does not exist!')
        if isinstance(error, commands.errors.DisabledCommand):
            await ctx.send(f'This command is disabled.')
        if isinstance(error, commands.errors.TooManyArguments):
            await ctx.send('There are too many arguments in the command!')
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send('This command is on cooldown.')
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('Member Not Found.')
        if isinstance(error, commands.errors.ChannelNotFound):
            await ctx.send('Channel Not Found')
        if isinstance(error, commands.errors.UserNotFound):
            await ctx.send('User Not Found')
        if isinstance(error, commands.errors.ChannelNotReadable):
            await ctx.send('I can\'t read messages from this channel.')
        if isinstance(error, commands.errors.RoleNotFound):
            await ctx.send('Role Not Found')
        if isinstance(error, commands.errors.EmojiNotFound):
            await ctx.send('Emoji Not Found')
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send('You are missing permissions to run this command!')
        if isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send('I am missing permissions to do this!')
        if isinstance(error, commands.errors.BotMissingAnyRole):
            await ctx.send('I are missing the roles to do this.')
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send('You are missing the roles do to this.')
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send('Turn on NSFW to use this command in this channel.')


for filename in listdir('C:\\Users\\pmpig\\Desktop\\Discord Bot\\cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

'''------------------------------------------------------------------------------------------------------------------'''

@commands.has_permissions(administrator=True)
@bot.command(name='load', help='| loads an unloaded category. similiar to enable/disable')
async def load_cogs(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.channel.send(f'{extension} was successfully loaded')

@commands.has_permissions(administrator=True)
@bot.command(name='unload', help='| Unloads a loaded category. similiar to enable/disable')
async def unload_cogs(ctx, extension):   
    bot.unload_extension(f'cogs.{extension}')    
    await ctx.channel.send(f'{extension} was successfully unloaded')

bot.run('Nzc0ODg0NzY1MjcwMTQ3MDgz.X6eRrA.eSpLPeQtQZkkqiQ-dYDaqZGh_XQ')
