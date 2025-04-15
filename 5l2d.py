"""
instagram-5letter-username-finder
Made by @xchup
"""

import asyncio
import random
import string
import os
import aiohttp
from pyfiglet import Figlet

# Telegram credentials
TOKEN = "7228420769:AAFo5KqJcXnoTh6CaYkW0ZRjnHXr3IW_E0E"
USER_ID = "1321020431"

# Setup UI
os.system("clear")
fig = Figlet(font='poison')
print("\033[1;36m" + fig.renderText("xchup"))
print("\033[1;33m🚀 IGHunt Started | Made by @xchup\n")

green = "\033[92m"
red = "\033[91m"
yellow = "\033[93m"

# Username format: NN.lD (N = digit, l = letter, D = digit)
async def generate_username():
    digits = ''.join(random.choices(string.digits, k=2))
    letter = random.choice(string.ascii_lowercase)
    last_digit = random.choice(string.digits)
    return f"{digits}.{letter}{last_digit}"

# Check availability on Instagram
async def check_username(session, username):
    headers = {
        "User-Agent": "Instagram 123.0.0.21.114",
    }
    url = f"https://www.instagram.com/{username}/?__a=1"
    async with session.get(url, headers=headers) as resp:
        return resp.status == 404

# Send to Telegram
async def send_to_telegram(username):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {
            "chat_id": USER_ID,
            "text": f"🔥 Available: `{username}`\n👤 Made by @xchup",
            "parse_mode": "Markdown"
        }
        await session.post(url, data=data)

# Main loop
async def hunt():
    async with aiohttp.ClientSession() as session:
        count = 0
        while True:
            try:
                username = await generate_username()
                is_available = await check_username(session, username)
                count += 1
                if is_available:
                    print(f"{green}[{count}] ✅ {username}")
                    await send_to_telegram(username)
                else:
                    print(f"{red}[{count}] ❌ {username}")
            except Exception as e:
                print(f"{yellow}⚠️ Error: {e}")
                await asyncio.sleep(2)

# Start
asyncio.run(hunt())
