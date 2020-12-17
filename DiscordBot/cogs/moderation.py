import discord
from discord import colour
from discord import channel
from discord import embeds
from discord.ext import commands

space = ' '

class Moderation(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| Removes given user from the server and blocks the user from joining again')
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban()
        
        enbed = discord.Embed(
            title=f'{ctx.message.author.name} has banned {member}',
            colour=discord.Colour.red(),
            description=f'{member} has been banned!'
            )
        enbed.add_field(name='Reason:', value=reason)
        await ctx.channel.send(embed=enbed)

        inbed = discord.Embed(
            title=f'You have been banned from{member.guild.name}!',
            description=f'You have been banned for {reason}',
            colour=discord.Colour.red()
            )
        await member.send(embed=inbed)

    @commands.has_permissions(kick_members=True)
    @commands.command(help='| Removes given user from the server')
    async def kick(self, ctx, Member:discord.Member, *, Reason=None):
        await Member.kick()
        enbad = discord.Embed(
            title=f'{ctx.message.author.mention} has kicked {Member.mention}',
            description=f'{Member} has been kicked!\n**Reason:**{Reason}',
            colour=discord.Colour.red()
            )
        await ctx.channel.send(embed=enbad)

    @commands.has_permissions(manage_messages=True)
    @commands.command(name='clear', help='| deletes an amount of messages, default is 1')
    async def messages_bulk_delete(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| unblocks a user that was banned from joining')
    async def unban(self, ctx, *, user:discord.user):

        try:
            bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
            if user in bans:
                await ctx.guild.unban(user)
            else:
                await ctx.send("User not banned!")
                return
        except discord.Forbidden:
            await ctx.send("I do not have permission to unban!")
            return
        except:
            await ctx.send("Unbanning failed!")
            return
        else:
            await ctx.send(f"Successfully unbanned {user.mention}!")

    @commands.has_permissions(ban_members=True)
    @commands.command(help='| Temporarily bans a member')
    async def tempban(self, ctx, member:discord.Member, reason, time):
        ban_embed = discord.Embed(
            title='Temp-Ban',
            description=f'{ctx.message.author} has banned {member.name}!'
        )
        ban_embed.add_field(name='Reason: ')
        ban_embed.add_field(value=reason)

        await ctx.send(embed=ban_embed)




def setup(client):
    client.add_cog(Moderation(client))