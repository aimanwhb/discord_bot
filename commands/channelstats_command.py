from discord.ext import commands
from discord.ext.commands import BucketType
import discord

class ChannelStatsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_counts = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            channel_id = str(message.channel.id)
            self.channel_counts[channel_id] = self.channel_counts.get(channel_id, 0) + 1

    @commands.command(name='channelstats')
    @commands.cooldown(1, 30, BucketType.guild)
    async def channel_stats(self, ctx):
        """Displays channel statistics"""
        sorted_channels = sorted(self.channel_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        embed = discord.Embed(title="📊 Channel Statistics", color=0x00ff00)
        for channel_id, count in sorted_channels:
            channel = self.bot.get_channel(int(channel_id))
            embed.add_field(name=f"#{channel.name}", value=f"{count} messages", inline=False)

        await ctx.send(embed=embed)