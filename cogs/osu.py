import discord
import borgor
import requests
from discord.ext import commands
from borgor import akatsukiapi
from typing import Optional
import config

class Osu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['osu', 'p'])
    async def profile(self, ctx, *, username):
        e = requests.get(f"https://osu.ppy.sh/api/get_user?k={config.osu_key}&u={username}")
        e_dictionary, = e.json()
        acc1 = float(e_dictionary['accuracy'])
        acc = round(acc1, 2)

        e_embed = discord.Embed(title=f"osu!standard stats for " + e_dictionary['username'], description="**Global Rank**: #" + e_dictionary['pp_rank'] + " (#" + e_dictionary['pp_country_rank'] + ")\n**PP**: " + e_dictionary['pp_raw']  + "\n**Accuracy**: " + str(acc) + "%" + "\n**Playcount**: " + e_dictionary['playcount'] + "\n\n**300s tapped**: " + e_dictionary['count300'] + "\n**100s tapped**: " + e_dictionary['count100'] + "\n**50s tapped**: " + e_dictionary['count50'])
        e_embed.set_thumbnail(url="https://a.ppy.sh/" + e_dictionary['user_id'])
        e_embed.set_footer(text="Joined on " + e_dictionary['join_date'] + " • " + e_dictionary['country'])
        await ctx.send(embed=e_embed)


    @commands.command(aliases=['t', 'osutop'])
    async def top(self, ctx, *, username):
        e = requests.get(f"https://osu.ppy.sh/api/get_user_best?k={config.osu_key}&u={username}")
        edict = e.json()

        g = requests.get(f"https://osu.ppy.sh/api/get_user?k={config.osu_key}&u={username}")
        gdict = g.json()[0]

        desc = []
        for index, score in enumerate(edict):
            f = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={config.osu_key}&b={score['beatmap_id']}")
            fdict = f.json()[0]
            sr = round(fdict["difficultyrating"])

            desc.append(f'**{index + 1}:** {fdict["artist"]} - {fdict["title"]} [{fdict["version"]}] ({sr} stars) | ')

        e_embed = discord.Embed(title=f"osu!standard tops for " + gdict['username'], description="\n".join(desc))
        e_embed.set_thumbnail(url="https://a.ppy.sh/" + gdict['user_id'])
        e_embed.set_footer(text="Joined on " + gdict['join_date'])
        await ctx.send(embed=e_embed)

def setup(bot):
    bot.add_cog(Osu(bot))
