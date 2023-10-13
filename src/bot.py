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


@bot.command(name='svn-help', description='Ping the bot')
async def help(ctx):
    """Ping the bot"""
    logging.info("Received command from discord")
    await ctx.send('This Help Message')

@bot.command(name='svn', description='Find any github issues with the given search term')
async def search_send(ctx, *args):
    """Search for new issues and send to discord"""
    logging.info("Received help command from discord")
    
    # automatically parse all the arguments
    params = ' '.join(args)
    results = await searcher.search(params)
    if results:
        for result in results:
            await ctx.send(result.html_url)
    else:
        await ctx.send("No issues found")

if __name__ == '__main__':
    """Start the bot"""
   
    bot.run(BOT_TOKEN)