import asyncio
import telegram
from random import choice
import os
from dotenv import load_dotenv


async def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    
    bot = telegram.Bot(TELEGRAM_TOKEN)    
    bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=open(f'images/{choice(os.listdir("images"))}', 'rb'))


if __name__ == '__main__':
    asyncio.run(main())
