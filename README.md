# SavannaBot

A discord bot to find Github's good first issue on different repositories.

## Get it

You can add the bot to your server by clicking on [<img alt="discord" width="100px" src="assets/discord.png"/>](https://discord.com/api/oauth2/authorize?client_id=1138189651593674845&permissions=274877908992&scope=bot)

## Configuration

- You will need your discord bot token. See how to get yours [here](https://discordpy.readthedocs.io/en/stable/discord.html)
- And your GitHub developer token. See how to get yours [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Now you need to change the `.env-example` to `.env`, with the following content.

```env
  GITHUB_TOKEN=<your GitHub developer access token>
  BOT_TOKEN=<your discord bot token>
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/angolaosc/savanna-bot.git
```

Go to the project directory:

```bash
  cd savanna-bot
```

Create your virtual environment:

```bash
  virtualenv env
```

and 

```bash
  source venv/bin/activate (in Linux)
```

Install the dependencies

```bash
  pip install -r requirements.txt
```
Now you are ready to go, run

```bash
  python3 src/bot.py
```

## Contributing

Contributions are always welcome!

See `CONTRIBUTING.md` for ways to get started.

## License
Savanna-bot is licensed under the [Apache License](./LICENSE), Version 2.0

---

Savanna-bot is a <a href="http://github.com/angolasc">Angola Open-source Community</a> open project.

![Angola Open-source Community ><](./assets/aosc.png)

## Code of Conduct(CoC)

Please note Savanna-bot follows the [AOSC Code of Conduct](https://github.com/angolaosc/.github/blob/main/CODE_OF_CONDUCT.md). By participating in this project, you agree to follow its terms.
