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
async def repeat(ctx, first_command: str, first_parameter: str, second_command: str = "", second_parameter: str = "", third_command: str = "", third_parameter: str = ""):
        arguments = [first_command, first_parameter.capitalize(), second_command, second_parameter.capitalize(), third_command, third_parameter.capitalize()]
        dex = Converter(arguments)
        dex.setFilters()
        command = first_command + second_command + third_command
        parameter = first_parameter + second_parameter + third_parameter
        if "-h" in command or "help" in parameter:
            data = dex.helpSelector()
        else:
            data = dex.ParseAllLocationData()
        if 0 < len(data) <= 2000:
            await ctx.send(data)
        elif len(data) > 2000:
            with open("outputFile.txt", "w") as f:
                f.write(data)
            await ctx.send(file=disnake.File('outputFile.txt'))
        else:
            await ctx.send("Please enter a valid parameter! For example, if entering a region make sure it is spelt correctly!")

bot.run('Your-token-here')
