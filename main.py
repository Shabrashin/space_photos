import asyncio
import telegram
import os
from dotenv import load_dotenv
import time


async def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    SENDING_FREQUENCY = os.getenv('SENDING_FREQUENCY')

    bot = telegram.Bot(TELEGRAM_TOKEN)  
    for root, dirs, files in os.walk('images'):
        for filename in files:
            bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=open(f'images/{filename}', 'rb'))
            time.sleep(int(SENDING_FREQUENCY))


if __name__ == '__main__':
    asyncio.run(main())
