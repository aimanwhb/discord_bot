from discord.ext import commands
from components.dropd import DropdownView

class MenuCommand(commands.Cog):
    """Cog for the menu command"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="menu")
    async def menu(self, ctx):
        """Sends a message with our dropdown"""

        # Create the view containing our dropdown
        view = DropdownView()

        # Sending a message and insert dropdown
        message = await ctx.send('Welcome to our discord!', view=view)

        # Disable dropdown once timeout
        await view.disable_after_timeout(message)
        await ctx.send('Timeout! Please try again.')