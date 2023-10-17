import logging
from typing import Tuple
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

locales = {
    "linguagem": "language",
    "dono": "owner",
    "actualização": "updated",
    "criado": "created",
}

@bot.event
async def on_ready():
    """Log when bot is ready"""
    logging.info(f'{bot.user} has connected to Discord!')
    logging.info("Starting SavannaBot")


@bot.command(name='svn', description='Find any github issues with the given search term')
async def search_send(ctx, *args):
    """Search for new issues and send to discord"""
    logging.info("Received command from discord")

    queries = translate_queries(args)

    # automatically parse all the arguments
    params = ' '.join(queries)
    results = await searcher.search(params)
    if results:
        for result in results:
            await ctx.send(result.html_url)
    else:
        await ctx.send("No issues found")


def translate_queries(args: Tuple[str]):
    query_parts = list(args)
    for q_part in query_parts:
        query = q_part.split(":")
        if query[0] in locales.keys():
            new_query = f"{locales[query[0]]}:{query[1]}"
            query_parts.remove(q_part)
            query_parts.append(new_query)
    return query_parts


if __name__ == '__main__':
    """Start the bot"""

    bot.run(BOT_TOKEN)
