import os
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, intents):
        super().__init__(command_prefix=commands.when_mentioned_or("!"), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('-----------------------------------------------')

        for guild in self.guilds:
            if guild.name == os.environ.get("DISCORD_GUILD"):
                break

        print(
            f'{self.user} is connected to the {guild.name} guild:\n'
        )

        members = [member.name for member in guild.members]
        print(f'Guild Members: {members}')