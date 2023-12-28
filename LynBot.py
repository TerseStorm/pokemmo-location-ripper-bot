import disnake
import random
import time
from disnake import app_commands, Permissions, Colour, Embed
from disnake.ext import commands
from convert_new import Converter
intents = disnake.Intents.all()
bot = commands.InteractionBot(intents=intents)
commands.CommandSyncFlags()

@bot.event
async def on_ready():
    print("bot is ready")
    print("Your-oauth-link-here")



        

@bot.slash_command(name = "location_finder", description = "Please work")
async def repeat(ctx, command: str, parameter: str):
        arguments = [command, parameter.capitalize()]
        dex = Converter(arguments)
        dex.setFilters()
        if "-h" in command or parameter=="help":
            data = dex.helpSelector()
        else:
            data = dex.ParseAllLocationData()
        if 0 < len(data) <= 2000:
            await ctx.send(data)
        elif len(data) > 2000:
            with open("outputFile.txt", "w") as f:
                f.write(data)
            await channel.send(file=disnake.File('outputFile.txt'))
        else:
            await ctx.send("Please enter a valid parameter! For example, if entering a region make sure it is spelt correctly!")

bot.run('Your-token-here')
