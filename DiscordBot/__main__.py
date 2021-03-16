from __init__ import  *

#in shell do pip install dnspython akinator.py[fast_async]
#add to server with https://discord.com/api/oauth2/authorize?client_id=774884765270147083&permissions=8&scope=bot
MClient = ''
Mdb = ''
servers = ''

def get_prefix(client, message):
    try:
        _id = message.guild.id
        e = dict(servers.find_one({'_id': _id}))

        return e['prefix']
    except Exception as we:
        print(we)

        
creator = 'The_Void#0156'
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=discord.Intents.all(), help_command=None)
space = ' '
e = '👀'

@bot.event
async def on_connect():
    print(f'{bot.user.name} has connected to Discord!')

@tasks.loop(minutes=22)
async def change_status():
    await bot.change_presence(activity=next(statuses))

@bot.event
async def on_guild_join(guild):
    try:    
        data = {'_id': str(guild.id), 'prefix': 't.', "blacklisted": []}
        servers.insert_one(data)
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    guild = member.guild
    
    if guild.id == 788831436584517722:
        await member.add_role(guild.get_role(807852371547258890))

    if guild.id == 787044308938391593:
        await member.add_role(guild.get_role(788245039171764306))

@bot.event
async def on_guild_remove(guild):
    servers.delete_one({"_id": guild.id})
    
@bot.event 
async def on_ready():
    global MClient, Mdb, servers

    change_status.start()
    print(f'Logged in as {bot.user.name}', 'Discord server: https://tinyurl.com/yxm3elzm', 'Command Prefix: "t."', sep='\n')

    MClient = MongoClient(f"mongodb+srv://{db['mongodb_username']}:{db['mongodb_password']}@{db['mongodb_cluster']}/Discord?retryWrites=true&w=majority")
    Mdb = MClient.Discord
    servers = Mdb.servers

@bot.event
async def on_message(message):
    message_content = message.content

    if message.author == bot.user:
        return

    if message.author.bot:
        return

    if 'nigger' in message_content.replace(" ", '').lower():
        await message.delete()
        await message.channel.send('DONT SAY THE N-WORD >:(')

    #if any(ext.lower() in message_content.lower() for ext in badwords[str(message.guild.id)]):
    #    await message.delete()

    await bot.process_commands(message=message)

@bot.event
async def on_message_delete(message):
    author = message.author
    integer = random.randint(1, 100)
    
    now = str(dt.datetime.now())

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
    if user.bot:
        return

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, discord.HTTPExeption):
        await ctx.send('Command Failed')

    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send('I dont have permission to do this!')

    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You\'re missing a reqiured argument for this command!')

    elif isinstance(error, commands.errors.PrivateMessageOnly):
        await ctx.send('This command only works in private messages!')

    elif isinstance(error, commands.errors.NoPrivateMessage):
        await ctx.send('bruh why are you trying this command here it doesnt work. jeez i work too much')

    elif isinstance(error, commands.errors.DisabledCommand):
        await ctx.send(f'An admin has disabled this command.')

    elif isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.send('This command is on cooldown.')

    elif isinstance(error, commands.errors.MemberNotFound):
        await ctx.send('Member Not Found.')

    elif isinstance(error, commands.errors.ChannelNotFound):
        await ctx.send('Channel Not Found')

    elif isinstance(error, commands.errors.UserNotFound):
        await ctx.send('User Not Found')

    elif isinstance(error, commands.errors.RoleNotFound):
        await ctx.send('Role Not Found')

    elif isinstance(error, commands.errors.EmojiNotFound):
        await ctx.send('Emoji Not Found')

    elif isinstance(error, commands.errors.MissingPermissions):
        await ctx.send('You are missing permissions to run this command!')

    elif isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.send('I am missing permissions to do this!')

    elif isinstance(error, commands.errors.BotMissingAnyRole):
        await ctx.send('I are missing the roles to do this.')

    elif isinstance(error, commands.errors.MissingAnyRole):
        await ctx.send('You are missing the roles do to this.')

    elif isinstance(error, commands.errors.NSFWChannelRequired):
        await ctx.send('Turn on NSFW to use this command in this channel.')


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
async def unload(ctx, extension: str):
    if extension != 'general' or extension != 'help':
        try:
            bot.unload_extension(f'cogs.{extension}')
        except:
            await ctx.send(f'{extension} was successfully unloaded')
        else:
            await ctx.send(f'{extension} was successfully loaded')

    else:
        await ctx.send(f'Cannot unload extension "{extension}"')

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
