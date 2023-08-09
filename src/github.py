from datetime import datetime, timedelta
from aiohttp import ClientSession
from models.issue import GoodFirstIssue
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class GithubSearcher:
    """Search for good first issues on github"""

    def __init__(self, github_token: str):
        self.github_token = github_token
        self.headers = {'Authorization': f'token {self.github_token}'}
        self.params = {'q': f'is:issue is:open label:"good first issue" created:>{self.current_date()}', 
                       'sort': 'updated', 
                       'order': 'asc',
                       'per_page': 5}
        self.url = 'https://api.github.com/search/issues'

    
    async def search(self) -> List[GoodFirstIssue]:
        """Search for good first issues on github"""
        results = []
        async with ClientSession() as session:
            logging.info("Searching for new issues")
            async with session.get(self.url, headers=self.headers, params=self.params) as response:
                if response.status == 200:
                    logging.info("search done, parsing data")
                    data = await response.json()
                    if data['items']:
                        results = [GoodFirstIssue(**item) for item in data['items'][:5]]
                    else:
                        logging.warning("No issues found")
                else:
                    logging.error("Error while searching issues")

        return results

    def current_date(self):
        """Return the current date minus 7 days"""
        return (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')