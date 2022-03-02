import discord
import borgor
import requests
from discord.ext import commands
from borgor import akatsukiapi
from typing import Optional
import config
from datetime import datetime as dt
import time

from utils.const import GRADES

class Osu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['osu', 'p'])
    async def profile(self, ctx, *, username):
        e = requests.get(f"https://osu.ppy.sh/api/get_user?k={config.osu_key}&u={username}")
        edict, = e.json()
        acc1 = float(edict['accuracy'])
        acc = round(acc1, 2)

        e_embed = discord.Embed(title=f"osu!standard stats for " + edict['username'], description="**Global Rank**: #" + edict['pp_rank'] + " (#" + edict['pp_country_rank'] + ")\n**PP**: " + edict['pp_raw']  + "\n**Accuracy**: " + str(acc) + "%" + "\n**Playcount**: " + edict['playcount'] + "\n\n**300s tapped**: " + edict['count300'] + "\n**100s tapped**: " + edict['count100'] + "\n**50s tapped**: " + edict['count50'])
        e_embed.set_thumbnail(url="https://a.ppy.sh/" + edict['user_id'])
        e_embed.set_footer(text="Joined on " + edict['join_date'] + " • " + edict['country'])
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
            sr1 = float(fdict['difficultyrating'])
            sr = round(sr1, 2)

            rank = score['rank']
            grade = GRADES[rank]

            date = score['date']
            date_format = dt.strptime(date, "%Y-%m-%d %H:%M:%S")
            ts1 = dt.timestamp(date_format)
            ts2 = time.time()
            
            diff = (float(ts2)-float(ts1))/(60*60*24)
            rounded_diff = round(diff)

            seconds = rounded_diff * 86400
            months = seconds / 2629746
            final_diff = round(months)

            pp1 = float(score['pp'])
            pp = round(pp1, 2)
            misses = score['countmiss']

            country = gdict['country'].lower()
                
            desc.append(f'**{index + 1}:** {grade} **{fdict["artist"]} - {fdict["title"]}** [{fdict["version"]}] ({sr} stars) • {pp}pp, {misses} misses, set {final_diff} months ago')
            e_embed = discord.Embed(title=f"osu!standard tops for " + gdict['username'], description="\n".join(desc))
            # e_embed.set_image(url=f"https://flagcdn.com/h20/{country}.png")
            e_embed.set_thumbnail(url="https://a.ppy.sh/" + gdict['user_id'])
            e_embed.set_footer(text="Joined on " + gdict['join_date'])
            await ctx.send(embed=e_embed)

def setup(bot):
    bot.add_cog(Osu(bot))
