from discord.ext import commands
from datetime import datetime
import discord

class UptimeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()

    @commands.command(name='uptime')
    async def uptime(self, ctx):
        """Shows bot uptime"""
        delta = datetime.now() - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed = discord.Embed(title="⏳ Bot Uptime", color=0x00ff00)
        embed.add_field(name="Uptime", value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)

        await ctx.send(embed=embed)