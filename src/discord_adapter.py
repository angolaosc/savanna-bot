from discord_webhook import DiscordWebhook, DiscordEmbed
from models.issue import GoodFirstIssue

class RequestsWebhookAdapter:
    """Adapter to convert the issue to a discord message"""

    def __init__(self, url: str):
        self.url = url
        self.webhook = DiscordWebhook(url=url)
    
    def post(self, data: GoodFirstIssue):
        """execute the webhook"""
        self.parse(data)
        return self.webhook.execute()
    
    def parse(self, data: GoodFirstIssue):
        """add embed to webhook from issue"""

        embed = DiscordEmbed(title=data.title, description='Voila, Encontramos um good-first issue! Checka agora', color=242424)
        embed.set_author(name='SavannaBot', url='https://github.com/angolaosc', icon_url=data.user['avatar_url'])
        embed.set_footer(text='AOSC', icon_url="https://raw.githubusercontent.com/angolaosc/mentorship/main/site/assets/logo.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Issue', value=data.html_url)
        embed.add_embed_field(name='Estado', value=data.state)
        #embed.add_embed_field(name='Number', value=f"#{data.issue_number}")

        # add embed object to webhook
        self.webhook.add_embed(embed)

