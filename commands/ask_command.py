from discord.ext import commands

class AskCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ask')
    async def uptime(self, ctx):

        await ctx.send("AI response")