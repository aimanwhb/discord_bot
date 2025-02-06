from discord.ext import commands
from discord.ext.commands import BucketType
import discord

class UserStatsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_counts = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            user_id = str(message.author.id)
            self.user_counts[user_id] = self.user_counts.get(user_id, 0) + 1

    @commands.command(name='userstats')
    @commands.cooldown(1, 30, BucketType.user)
    async def user_stats(self, ctx, user: discord.Member = None):
        """Displays user statistics"""
        user = user or ctx.author
        count = self.user_counts.get(str(user.id), 0)

        embed = discord.Embed(title="📊 User Statistics", color=0x00ff00)
        embed.add_field(name="User", value=user.mention, inline=False)
        embed.add_field(name="Messages Sent", value=count, inline=False)

        await ctx.send(embed=embed)