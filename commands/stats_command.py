from discord.ext import commands
from datetime import datetime
import discord

class StatsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        self.message_count = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            self.message_count += 1

    @commands.command(name='stats')
    async def stats(self, ctx):
        """Displays server statistics"""
        guild = ctx.guild

        # Calculate uptime
        uptime = datetime.now() - self.start_time

        # Get online members
        online_members = [member for member in guild.members
                         if not member.bot and member.status != discord.Status.offline]

        # Create embed
        embed = discord.Embed(
            title="📊 Server Statistics",
            color=0x00ff00,
            description=f"Tracking since {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        embed.add_field(name="Total Messages", value=self.message_count, inline=True)
        embed.add_field(name="Members Online", value=f"{len(online_members)}/{guild.member_count}", inline=True)
        embed.add_field(name="Bot Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)

        # Show top 5 online members
        online_list = "\n".join([f"{member.mention} ({member.status})" for member in online_members[:5]])
        if online_list:
            embed.add_field(name="Online Members", value=online_list, inline=False)

        embed.set_footer(text=f"Server Uptime: {str(uptime).split('.')[0]}")

        await ctx.send(embed=embed)