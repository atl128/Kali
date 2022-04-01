import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int = 0):
        if amount == None
            await ctx.send('You must provide an amount!', delete_after=5)
        else if amount == 0:
            await ctx.send('Amount must be more than 0.', delete_after=5)
        else:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'{ctx.author.mention} purged {amount} messages in {ctx.channel.mention}.')

@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')

@commands.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, reason=None):
    await member.unban(reason=reason)
    await ctx.send(f'{member.mention} has been unbanned.')

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, reason: str = None):
        for mention in user:
            await mention.kick(reason=reason)
            return await ctx.send(f'{mention} has been kicked.')

def setup(bot):
    bot.add_cog(Moderation(bot))
