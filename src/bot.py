import logging
import discord
from pathlib import Path
from decouple import config
from discord.ext import commands
from github import GithubSearcher

root = Path(__name__).parent

# config logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# get config values
BOT_TOKEN = config("BOT_TOKEN", cast = str)
CHANNEL_ID = config("DISCORD_CHANNEL_ID", cast = int)
GITHUB_TOKEN = config("GITHUB_TOKEN", cast = str)

# create intents for bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# create bot object
bot = commands.Bot(command_prefix='/', description='SavannaBot', case_insensitive=True, intents=intents)
searcher = GithubSearcher(github_token=GITHUB_TOKEN)

@bot.event
async def on_ready():
    """Log when bot is ready"""
    logging.info(f'{bot.user} has connected to Discord!')
    logging.info("Starting SavannaBot")


@bot.command(name='svn', description='Find any github issues with the given search term')
async def search_send(ctx, *args):
    """Search for new issues and send to discord"""
    logging.info("Received command from discord")
    
    # automatically parse all the arguments
    params = ' '.join(args)
    results = await searcher.search(params)
    if results:
        for result in results:
            await ctx.send(result.html_url)
    else:
        await ctx.send("No issues found")

@bot.command(name='help', description="Retrieve information about the available commands and their usage")
def show_help():
    """Display a list of available commands and get information on how to use the Savanna Bot"""
    logging.info("""
        Description: An example program to demonstrate how to organize help in the command-line interface.

        Usage:
        MyProgramCLI --option1 VALUE --option2 VALUE
        
        Options:
        --option1 VALUE      Option to perform Task 1.
                            Example: MyProgramCLI --option1 value1

        --option2 VALUE      Option to perform Task 2.
                            Example: MyProgramCLI --option2 value2

        --help               Show this help message and exit.
        
        Examples:
        - Perform Task 1:
            MyProgramCLI --option1 value1

        - Perform Task 2:
            MyProgramCLI --option2 value2
        """)
    

if __name__ == '__main__':
    """Start the bot"""
   
    bot.run(BOT_TOKEN)