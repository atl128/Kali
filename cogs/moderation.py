import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int = 0):
        if amount == 0:
            await ctx.send('You must provide an amount!', delete_after=5)
        else:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'{ctx.author.mention} purged {amount} messages in {ctx.channel.mention}!', delete_after=5)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned!')

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, reason=None):
    await member.unban(reason=reason)
    await ctx.send(f'{member.mention} has been unbanned!')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, reason: str = None):
        for mention in user:
            await mention.kick(reason=reason)
            return await ctx.send(f'{mention} has been kicked!')

def setup(bot):
    bot.add_cog(Moderation(bot))
