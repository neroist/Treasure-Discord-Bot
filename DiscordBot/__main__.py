from __init__ import  *

#in shell do pip install dnspython akinator[fast_async]

#MClient = pymongo.MongoClient(f"mongodb+srv://{db['mongodb_username']}:{db['mongodb_password']}@{db['mongodb_cluster']}/Discord?retryWrites=true&w=majority")
#Mdb = MClient.Discord
#prefixes = Mdb.prefixes

badwords = []

def get_prefix(client, message):
    with open("DiscordBot/prefixes.json") as file:
        thx = json.load(file)
        file.close()

    return thx[str(message.guild.id)]

creator = 'The_Void#0156'
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=discord.Intents.all(), help_command=None)
space = ' '

@bot.event
async def on_connect():
    print(f'{bot.user.name} has connected to Discord!')

@tasks.loop(minutes=22)
async def change_status():
    await bot.change_presence(activity=next(statuses))

@tasks.loop(minutes=5)
async def update_blacklisted():
    global badwords

    with open('DiscordBot/cogs/blacklisted.json') as file:
        b = json.load(file)
        file.close()

    badwords=b

@bot.event
async def on_guild_join(guild):

    with open("DiscordBot/prefixes.json", 'r+') as file:
        thx = json.load(file)
        thx[str(guild.id)] = "t."

        file.seek(0)
        json.dump(thx, file, indent=4)
        file.close()
        

@bot.event
async def on_guild_remove(guild):

        with open("DiscordBot/prefixes.json", 'r+') as file:
            thx = json.load(file)
            thx.pop(str(guild.id))

            file.seek(0)
            json.dump(thx, file, indent=4)
            file.close()

@bot.event 
async def on_ready():
    change_status.start()
    print(f'Logged in as {bot.user.name}', 'Discord server: https://tinyurl.com/yxm3elzm', 'Command Prefix: "."', sep='\n')

@bot.event
async def on_message(message):
    message_content = message.content

    if message.author == bot.user:
        return

    if message.author.bot:
        return

    if message_content.isupper() == True and len(message_content) >= 6:
        await message.channel.send(f'**{message.author.name}** chill with the caps')
        await asyncio.sleep(1.5)
        await message.delete()

    if 'nigger' in message_content.replace(" ", ''):
        await message.delete()
        await message.channel.send('DONT SAY THE N-WORD >:(')

    if any(ext.lower() in message_content.lower() for ext in badwords):
        await message.delete()

    await bot.process_commands(message=message)

@bot.event
async def on_message_delete(message):
    author = message.author
    integer = random.randint(1, 1000)
    
    now = str(dt.datetime.now())
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
async def on_reaction_add(reaction, user):

    if user == bot.user:
        return

    if user.bot:
        return


#@bot.event
#async def on_command_error(ctx, error):
#    if isinstance(error, discord.HTTPExeption):
#        await ctx.send('Command Failed')
#    elif isinstance(error, discord.errors.Forbidden):
#        await ctx.send('I dont have permission to do this!')
#    elif isinstance(error, commands.errors.MissingRequiredArgument):
#        await ctx.send('You\'re missing a reqiured argument for this command!')
#    elif isinstance(error, commands.errors.PrivateMessageOnly):
#        await ctx.send('This command only works in private messages!')
#    elif isinstance(error, commands.errors.NoPrivateMessage):
#        await ctx.send('bruh why are you trying this command here it doesnt work. jeez i work too much')
#    elif isinstance(error, commands.errors.DisabledCommand):
#        await ctx.send(f'An admin has disabled this command.')
#    elif isinstance(error, commands.errors.CommandOnCooldown):
#        await ctx.send('This command is on cooldown.')
#    elif isinstance(error, commands.errors.MemberNotFound):
#        await ctx.send('Member Not Found.')
#    elif isinstance(error, commands.errors.ChannelNotFound):
#        await ctx.send('Channel Not Found')
#    elif isinstance(error, commands.errors.UserNotFound):
#        await ctx.send('User Not Found')
#    elif isinstance(error, commands.errors.RoleNotFound):
#        await ctx.send('Role Not Found')
#    elif isinstance(error, commands.errors.EmojiNotFound):
#        await ctx.send('Emoji Not Found')
#    elif isinstance(error, commands.errors.MissingPermissions):
#        await ctx.send('You are missing permissions to run this command!')
#    elif isinstance(error, commands.errors.BotMissingPermissions):
#        await ctx.send('I am missing permissions to do this!')
#    elif isinstance(error, commands.errors.BotMissingAnyRole):
#        await ctx.send('I are missing the roles to do this.')
#    elif isinstance(error, commands.errors.MissingAnyRole):
#        await ctx.send('You are missing the roles do to this.')
#    elif isinstance(error, commands.errors.NSFWChannelRequired):
#        await ctx.send('Turn on NSFW to use this command in this channel.')


for filename in os.listdir('DiscordBot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@commands.has_permissions(administrator=True)
@bot.command(help='| loads an unloaded category. similiar to enable/disable')
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
    except:
        await ctx.send('Something went wrong')
    else:
        await ctx.send(f'{extension} was successfully loaded')

@commands.has_permissions(administrator=True)
@bot.command(help='| Unloads a loaded category. similiar to enable/disable')
async def unload(ctx, extension):   
    try:
        bot.unload_extension(f'cogs.{extension}')
    except:
        await ctx.send('Something went wrong')
    else:
        await ctx.send(f'{extension} was successfully unloaded')

@commands.has_permissions(administrator=True)
@bot.command(help='| Reloads an loaded category')
async def reload(ctx, extension):
    try:
        bot.reload_extension(f'cogs.{extension}')
    except:
        await ctx.send('Something went wrong')
    else:
        await ctx.send(f'{extension} was successfully reloaded')

if __name__ == '__main__':
    from keep_alive import keep_alive
    keep_alive()
    bot.run(db['BOT_TOKEN'])