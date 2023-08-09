from aiohttp import ClientSession
from typing import List, Optional
import logging
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class GoodFirstIssue(BaseModel):
    """Model to represent a good first issue"""
    title: str
    html_url: Optional[str] = None
    state: Optional[str] = None
    issue_number: Optional[int] = None
    created_at: Optional[str] = None
    user: Optional[dict] = None

class GithubSearcher:
    """Search for good first issues on github"""

    def __init__(self, github_token: str):
        self.github_token = github_token
        self.headers = {'Authorization': f'token {self.github_token}'}
        self.url = 'https://api.github.com/search/issues'

    
    async def search(self, q) -> List[GoodFirstIssue]:
        """Search for good first issues on github"""
        results = []

        async with ClientSession() as session:
            logging.info("Searching for new issues")
            
            params = {
                'q': f'is:issue is:open label:"good first issue" {q}',
                'sort': 'updated', 
                'order': 'asc',
                'per_page': 5}
            
            async with session.get(self.url, headers=self.headers, params=params) as response:
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