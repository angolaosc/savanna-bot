# savanna-bot

A discord bot to find github's good first issue on different repositories.

## Configuration

- You will need your discord channel's webhook link. See how to create [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) 
- And your github developer token. See how to get yours [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Now you need to change the `.env-example` to `.env`, with the following content

```env
  GITHUB_TOKEN=<your github developer access token>
  DISCORD_WEBHOOK_URL=<your discord channel's webhook link>
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/angolaosc/savanna-bot.git
```

Go to the project directory

```bash
  cd savanna-bot
```

Create your virtual environment

```bash
  virtualenv env
```

and 

```bash
  source venv/bin/activate (in Linux)
```

install the dependencies

```bash
  pip install -r requirements.txt
```
now you are ready to go, run

```bash
  python3 src/main.py
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
