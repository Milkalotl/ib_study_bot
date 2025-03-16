from typing import Final

import os
from discord import Intents, Embed, Interaction, app_commands
import asyncio
from itertools import cycle
from dotenv import load_dotenv
from responses import get_response, help_func 
from discord.ext import commands, tasks


load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.command()
async def bee(ctx, arg):
    response = get_response(arg, message.author.id)
    await ctx.send(embed=response)

@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {synced_commands}")
    except Exception as e:
        print("Error: ", e)

@bot.tree.command(name="bee", description="Please refer to /help for syntax")
async def bee(interaction: Interaction, arg:str, max_year:int=2023, min_year:int=2010, specific_year:int = None, paper:int=0, name:str=None, repetitions:int=1):
    if specific_year != None:
        max_year = specific_year
        min_year = specific_year
    response = get_response(arg, interaction.user.display_name, max_year, min_year, paper, name, repetitions)
    await interaction.response.send_message(embed=response)

@bot.tree.command(name="help", description="Run for help!")
async def help(interaction: Interaction):
    response = help_func()
    await interaction.response.send_message(embed=response)




def main():
    bot.run(token=TOKEN)

if __name__ == "__main__":
    main()
