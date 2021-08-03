import asyncio
from datetime import datetime, timedelta

import discord
from discord.ext import commands, tasks

from .utils.common import CommonUtil


class Moira(commands.Cog, name='Thread管理用cog'):
    """
    管理用のコマンドです
    """

    def __init__(self, bot):
        self.bot = bot
        self.c = CommonUtil()


    async def call_of_thread(self, thread: discord.Thread) -> None:
        role_ids = [829050613027307611, 871467886307340378, 872083918805946370]
        if role_ids is None:
            return

        content = ''

        for id in role_ids:
            role = thread.guild.get_role(id)
            if role is not None:
                content = f'{content}{role.mention}'

        msg = await thread.send("スレッドが作成されました")
        await msg.edit(content=f'{content} {msg.content}')

    @commands.Cog.listener()
    async def on_thread_join(self, thread: discord.Thread):
        if not thread.me:
            await thread.join()
            return

        await self.call_of_thread(thread)

        if thread.parent is not None:
            try:
                if thread.parent.slowmode_delay == 0:
                    return
                await thread.edit(slowmode_delay=thread.parent.slowmode_delay)
                msg = await thread.send("低速モードを設定しました")
                await self.c.autodel_msg(msg)
            except discord.Forbidden:
                print("権限不足")
                print(thread)

def setup(bot):
    bot.add_cog(Moira(bot))
