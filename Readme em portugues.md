# SavannaBot

Um bot do Discord para encontrar boas primeiras issues no GitHub em diferentes repositórios.

## Vamos a isso:

Você pode adicionar o bot ao seu servidor clicando em [<img alt="discord" width="100px" src="assets/discord.png"/>](https://discord.com/api/oauth2/authorize?client_id=1138189651593674845&permissions=274877908992&scope=bot)

## Como Usar

- `/svn <param>: <your query>` -  Buscar boas primeiras issues no GitHub
> Exemplo: `/svn language:python`
Os parâmetros da consulta são os mesmos usados na barra de pesquisa do GitHub. Veja a lista completa [here](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests).

Alguns dos parâmetros mais usados são:

- `owner` -  Filtrar pelo usuário que criou a issue.
- `language` - Filtrar pela linguagem em que o repositório está escrito.
- `label` - Filtrar pelas labels aplicadas à issue.
- `state` - Filtrar pelo estado da issue.
- `repo` - Filtrar pelo repositório ao qual a issue pertence.

Você também pode usar qualquer combinação dos parâmetros acima.
> Exemplo: `/svn owner:angolaosc language:python repo:angolaosc/savanna-bot`

## Configuração

- Você precisará do token do seu bot do Discord. Veja como obtê-lo aqui [aqui](https://discordpy.readthedocs.io/en/stable/discord.html)
- E do token de desenvolvedor do GitHub. Veja como obter o seu [aqui](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Agora, você precisa alterar o arquivo .env-example para .env, com o seguinte conteúdo.

```env
  GITHUB_TOKEN=<your GitHub developer access token>
  BOT_TOKEN=<your discord bot token>
```

## Executar localmente

Clone o repositorio

```bash
  git clone https://github.com/angolaosc/savanna-bot.git
```

Vá para o diretório do projeto:

```bash
  cd savanna-bot
```

Crie seu ambiente virtual:

```bash
  virtualenv env
```

e 

```bash
  source venv/bin/activate (in Linux)
```

Instale as dependências

```bash
  pip install -r requirements.txt
```
Agora você está pronto para ir, execute

```bash
  python3 src/bot.py
```

## Contribuição

Contribuições são sempre bem-vindas!

Veja `CONTRIBUTING.md`para saber como começar.

## Licença
Savanna-bot está licenciado sob a [Apache License](./LICENSE), Version 2.0

---

Savanna-bot is a <a href="http://github.com/angolasc">Angola Open-source Community</a> open project.

![Angola Open-source Community ><](./assets/aosc.png)

## Code of Conduct(CoC)

Please note Savanna-bot follows the [AOSC Code of Conduct](https://github.com/angolaosc/.github/blob/main/CODE_OF_CONDUCT.md). By participating in this project, you agree to follow its terms.

