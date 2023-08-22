import logging
import discord
from pathlib import Path
from decouple import config
from discord.ext import commands
from github import GithubSearcher

root = Path(__name__).parent

# config logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# get config values
BOT_TOKEN = config("BOT_TOKEN", cast=str)
CHANNEL_ID = config("DISCORD_CHANNEL_ID", cast=int)
GITHUB_TOKEN = config("GITHUB_TOKEN", cast=str)

# create intents for bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# create bot object
bot = commands.Bot(command_prefix='/', description='SavannaBot',
                   case_insensitive=True, intents=intents)
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

    if '--help' == args:
        show_help()
        return None

    # automatically parse all the arguments
    params = ' '.join(args)
    results = await searcher.search(params)
    if results:
        for result in results:
            await ctx.send(result.html_url)
    else:
        await ctx.send("No issues found")


async def show_help(ctx, *args):
    """Display a list of available commands and get information on how to use the Savanna Bot"""
    await ctx.send("""
            These are common SVN commands used in various situations:
                        
            #Search by language
                        
            With the language qualifier you can search for issues and pull requests within repositories that are written in a certain language.
            
            Qualifier:
            /svn language:LANGUAGE   Example: language:ruby state:open matches open issues that are in Ruby repositories.
                        
            #Search by when an issue or pull request was created or last updated

            When you search for a date, you can use greater than, less than, and range qualifiers to further filter results. For more information, see "Understanding the search syntax."

            Qualifier	
            /svn created:YYYY-MM-DD	Example: language:c# created:<2011-01-01 state:open matches open issues that were created before 2011 in repositories written in C#.

            /svn updated:YYYY-MM-DD Example: weird in:body updated:>=2013-02-01 matches issues with the word "weird" in the body that were updated after February 2013.   
            """)


if __name__ == '__main__':
    """Start the bot"""

    bot.run(BOT_TOKEN)
