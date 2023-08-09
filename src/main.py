import asyncio
import logging
from pathlib import Path
from decouple import config
from discord_adapter import RequestsWebhookAdapter
from github import GithubSearcher

root = Path(__name__).parent

# config logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# get config values
GITHUB_TOKEN = config("GITHUB_TOKEN", cast = str)
DISCORD_WEBHOOK_URL = config("DISCORD_WEBHOOK_URL", cast = str)

# create github and webhook objects
github = GithubSearcher(github_token=GITHUB_TOKEN)
webhook = RequestsWebhookAdapter(url=DISCORD_WEBHOOK_URL)

sleep_time = 60 * 60 * 24 # 24 hours

async def search_send():
    """Search for new issues and send to discord"""

    github_results = await github.search()
    if github_results: 
        logging.info("Sending message to discord")
        for result in github_results:
            webhook.post(result)


async def run_every_time():
    f"""Run search_send every {sleep_time} seconds"""
    while True:
        await search_send()
        logging.info(f"Waiting {sleep_time} seconds to search again")
        await asyncio.sleep(sleep_time)

async def main():
    """Run the bot"""
    asyncio.create_task(run_every_time())
    
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    """Start the bot"""
    logging.info("Starting SavannaBot")
    asyncio.run(main())
