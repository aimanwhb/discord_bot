import os
import discord
import logging
from dotenv import load_dotenv
from logger_config import LoggerConfig
from commands.menu_command import MenuCommand
from commands.bot import Bot
from commands.stats_command import StatsCommand
from commands.channelstats_command import ChannelStatsCommand
from commands.userstats_command import UserStatsCommand
from commands.leaderboard_command import LeaderboardCommand
from commands.uptime_command import UptimeCommand

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, LEVEL, logging.INFO)

intents = discord.Intents.all()

LoggerConfig.setup_logging()

async def main():
    bot = Bot(intents)
    await bot.add_cog(MenuCommand(bot))
    await bot.add_cog(StatsCommand(bot))
    await bot.add_cog(ChannelStatsCommand(bot))
    await bot.add_cog(UserStatsCommand(bot))
    await bot.add_cog(LeaderboardCommand(bot))
    await bot.add_cog(UptimeCommand(bot))
    await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())