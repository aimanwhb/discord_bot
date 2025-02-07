from discord.ext import commands
from features.ai_response import get_ai_response, split_message


class AskCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ask')
    async def Ask(self, ctx, * , query: str):

        response = get_ai_response(query)
        chunks = split_message(response)
        for chunk in chunks:
            await ctx.send(chunk)

        # await ctx.send(f"**Question:** {query}\n**Answer:** {response}")