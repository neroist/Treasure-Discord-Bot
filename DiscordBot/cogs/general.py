import discord
from discord.ext import commands
from discord.ext.commands import *

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(change_nickname=True, manage_nicknames=True)
    @commands.command(name='nick', help='| Changes a users nickname')
    async def change_user_nickname(self, ctx, member:discord.Member, *, nickname):
        await member.edit(nick=nickname)
        await ctx.send(f'Nickname was successfully changed for {member.mention} to {nickname}.')

    @commands.command(help='| gives info on given user')
    async def whois(self, ctx:Context, member:discord.Member):
        if member.is_on_mobile == True:
            device = 'Mobile'
        else:
            device = 'Computer'
        
        roles = member.roles[:-1]
        roles = ' '.join(roles)

        embed=discord.Embed(title="User Info", color=discord.Colour.purple())
        embed.add_field(name="Name:", value=str(member), inline=True)
        embed.add_field(name="Joined Guild:", value=member.joined_at, inline=True)
        embed.add_field(name="Bot:", value=member.bot, inline=True)
        embed.add_field(name='Status:', value=member.raw_status, inline=True)
        embed.add_field(name="Activity:", value=member.activity, inline=True)
        embed.add_field(name="Device:", value=device, inline=True)
        embed.add_field(name="Color:", value=member.colour, inline=True)
        embed.add_field(name='Roles:', value=roles, inline=True)
        embed.add_field(name='Top Role', value=member.top_role, inline=True)
        embed.add_field(name='Permissions:', value=member.guild_permissions, inline=True)
        embed.add_field(name='Id:', value=member.id, inline=True)

        embed.set_footer(text="Treasure • 12/14/2020")
        await ctx.send(embed=embed)
    





def setup(client):
    client.add_cog(General(client))