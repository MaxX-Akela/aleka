import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=disnake.command, intents=disnake.Intents.default())
intents = disnake.Intents.default()
intents.message_content = True

@bot.event
async def on_ready():
    print(" █████╗ ██╗     ███████╗██╗  ██╗ █████╗ ")
    print("██╔══██╗██║     ██╔════╝██║ ██╔╝██╔══██╗")
    print("███████║██║     █████╗  █████╔╝ ███████║")
    print("██╔══██║██║     ██╔══╝  ██╔═██╗ ██╔══██║")                  
    print("██║  ██║███████╗███████╗██║  ██╗██║  ██")
    print("╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝")
    print(f'Logged in as {bot.user}')
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("Clover or Clever ?"))


bot.load_extensions('cogs')


bot.run("")

