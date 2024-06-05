# Telegram GPT Bot

This is a Telegram bot that uses the a LLM model for generating responses. 

It's built with Python and uses the OpenAPI client to call [LM Studio](https://lmstudio.ai) running locally.

Your data never leaves your machine, and is setup so the bot only responds only to your tellegram account just set the `USER_ID` in the `.env` file to your telegram user id.

## Models

I used the following models for the bot for testing but you can use other models:

- `llamma 3 7b` 

## Dependencies

The project uses several dependencies, including:

- `pydantic`
- `pytelegrambotapi`
- `openai`
- `openai-whisper`
- `torch`

You can find the full list in the [`pyproject.toml`](pyproject.toml) file.

## Usage

To use the bot, you need to run the `main.py` script. Before running the script, make sure to set up your environment variables in the `.env` file. 

You can use the `.env.example` file as a template.

## Transcription

The bot uses the `transcribe` function from [`transcriber.py`](src/transcriber.py) to transcribe audio messages.

## Development

For development, the project uses `ruff`. It is installed as a dev dependency.

## Installing dependencies

The project uses Poetry for dependency management.  

```sh
poetry shell
poetry install
```

## Running the bot
```sh
python main.py
```

