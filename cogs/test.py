import discord
from discord.ext import commands
import time

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx: str):
        await ctx.send("にゃーん")

    @commands.command()
    async def pingtes(self, ctx):
        """Pingによる疎通確認を行うコマンド"""
        start_time = time.time()
        await ctx.send(content="pong!\n" + str(round(time.time() - start_time, 3) * 1000) + "ms")

def setup(bot):
    bot.add_cog(Test(bot))
