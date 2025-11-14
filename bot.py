import asyncio
from datetime import datetime
from pyrogram import Client
from pyrogram.enums import ParseMode
from aiohttp import web
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, PORT
from plugins import web_server
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

name = "Links Sharing Started"

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self, **kwargs):
        await super().start(**kwargs)
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot Running..!\n\nCreated by \nhttps://t.me/Okabe_xRintarou")
        self.LOGGER(__name__).info(f"{name}")
        self.username = usr_bot_me.username
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

    async def stop(self, *args, **kwargs):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

if __name__ == "__main__":
    Bot().run()
