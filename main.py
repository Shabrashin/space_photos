import asyncio
import telegram
import os
from dotenv import load_dotenv
import time


def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    telegram_channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    sending_frequency = os.getenv('SENDING_FREQUENCY')

    bot = telegram.Bot(telegram_token)  
    for root, dirs, files in os.walk('images'):
        for filename in files:
            bot.send_photo(chat_id=telegram_channel_id, photo=open(f'images/{filename}', 'rb'))
            time.sleep(int(sending_frequency))


if __name__ == '__main__':
    main()
