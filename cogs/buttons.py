from discord.ext.ui import Component, Button, View, ObservableObject, published, Message
from discord.ext import commands
import discord
import os


class SampleViewModel(ObservableObject):
    num = published('num')

    def __init__(self):
        super().__init__()
        self.num = 0

    def countup(self):
        self.num += 1

    def countdown(self):
        self.num -= 1


class SampleView(View):
    def __init__(self, bot):
        super().__init__(bot)
        self.view_model = SampleViewModel()

    async def add_reaction(self):
        await self.get_message().add_reaction("\U0001f44d")

    async def body(self):
        return Message(
            content=f"test! {self.view_model.num}",
            component=Component(items=[
                [
                    Button("+1")
                        .on_click(lambda x: self.view_model.countup())
                        .custom_id("aaa")
                        .style(discord.ButtonStyle.blurple),

                    Button("-1")
                        .on_click(lambda x: self.view_model.countdown())
                        .custom_id("iii")
                        .style(discord.ButtonStyle.blurple)
                ]
            ])
        )

class Dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='yellow', description='Your favourite colour is yellow', emoji='🟨',),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦')
        ]
        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Your favourite colour is {self.values[0]}', ephemeral=True)


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown())


class buttons(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def button(self, ctx: str):
        await SampleView(self.bot).start(ctx.channel)

    @commands.command()
    async def drop(self, ctx: str):
        await ctx.send('a', view=DropdownView())
        pass

def setup(bot):
    bot.add_cog(buttons(bot))
