from discord.ext import commands
from discord.ext.commands import BucketType
import discord

class LeaderboardCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_counts = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            user_id = str(message.author.id)
            self.user_counts[user_id] = self.user_counts.get(user_id, 0) + 1

    @commands.command(name='leaderboard')
    @commands.cooldown(1, 60, BucketType.guild)
    async def leaderboard(self, ctx):
        """Displays message leaderboard"""
        sorted_users = sorted(self.user_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        embed = discord.Embed(title="🏆 Message Leaderboard", color=0x00ff00)
        for idx, (user_id, count) in enumerate(sorted_users, 1):
            user = self.bot.get_user(int(user_id))
            embed.add_field(name=f"{idx}. {user.display_name}", value=f"{count} messages", inline=False)

        await ctx.send(embed=embed)