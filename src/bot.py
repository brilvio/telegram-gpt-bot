import os

import telebot

from .chat import ask_bot
from .settings import settings
from .transcriber import transcribe

bot = telebot.TeleBot(settings.telegram_token)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


def is_me(message):
    return message.from_user.id == int(settings.user_id)


@bot.message_handler(func=is_me, content_types=["text"])
def ask_gpt_text(message):
    response = ask_bot(message)

    bot.reply_to(message, response)


@bot.message_handler(func=is_me, content_types=["audio", "voice"])
def ask_gpt_audio(message):
    try:
        # Download the voice file
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_name = f"voice_{message.from_user.id}.ogg"

        # Save the file locally
        with open(file_name, "wb") as new_file:
            new_file.write(downloaded_file)

        # Transcribe the voice file
        transcription = transcribe(file_name)
        text = transcription["text"]

        response = ask_bot(text)

        # Send the transcribed text back to the user
        bot.reply_to(message, response)

        # Remove the file after processing
        os.remove(file_name)
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")


def init_bot():
    bot.infinity_polling()
