import os
import discord
import logging
from dotenv import load_dotenv
from logger_config import LoggerConfig
from commands.menu_command import MenuCommand
from commands.bot import Bot

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper() # logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).env
LOG_LEVEL = getattr(logging, LEVEL , logging.INFO)

intents = discord.Intents.all()

LoggerConfig.setup_logging()

async def main():
    bot = Bot(intents)
    await bot.add_cog(MenuCommand(bot))  # Await add_cog for !menu command
    await bot.start(TOKEN)

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())