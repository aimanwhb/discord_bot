import asyncio
import discord
import os
import json
from .dropd_logic import Userselection

user_selection = Userselection()

# Load json from dropdown.json file
with open("json/dropdown.json", "r") as file:
    data = json.load(file)

class Dropdown1(discord.ui.Select):
    def __init__(self):

        """
            Set the options that will be presented inside the dropdown
            The placeholder is what will be shown when no option is chosen
            The min and max values indicate we can only pick one of the three options
            The options parameter defines the dropdown options. We defined this above
        """

        self.name_placeholder = data["dd1"]["placeholder"]

        options = [
            discord.SelectOption(label=data["dd1"]["option1"]["label1"],
                                 description=data["dd1"]["option1"]["desc1"],
                                 emoji=data["dd1"]["option1"]["emoji1"]
                                 ),
            discord.SelectOption(label=data["dd1"]["option2"]["label2"],
                                 description=data["dd1"]["option2"]["desc2"],
                                 emoji=data["dd1"]["option2"]["emoji2"]
                                 ),
            discord.SelectOption(label=data["dd1"]["option3"]["label3"],
                                 description=data["dd1"]["option3"]["desc3"],
                                 emoji=data["dd1"]["option3"]["emoji3"]
                                 ),
        ]

        super().__init__(placeholder=self.name_placeholder,
                         min_values=1,
                         max_values=1,
                         options=options,
                         row=1
                         )

    async def callback(self, interaction: discord.Interaction):

        """
            Use the interaction object to send a response message containing
            the user's favourite colour or choice. The self object refers to the
            Select object, and the values attribute gets a list of the user's
            selected options. We only want the first one.
        """

        user_selection.update_selection(interaction.user.id, self.name_placeholder, self.values[0])
        await interaction.response.defer()
        # await interaction.response.send_message(f"You have selected {self.values[0]}")
        await user_selection.check(interaction, self.name_placeholder, self.values[0])


class Dropdown2(discord.ui.Select):
    def __init__(self):

        self.name_placeholder = data["dd2"]["placeholder"]

        options = [
            discord.SelectOption(label=data["dd2"]["option1"]["label1"],
                                 description=data["dd2"]["option1"]["desc1"],
                                 emoji=data["dd2"]["option1"]["emoji1"]
                                 ),
            discord.SelectOption(label=data["dd2"]["option2"]["label2"],
                                 description=data["dd2"]["option2"]["desc2"],
                                 emoji=data["dd2"]["option2"]["emoji2"]
                                 ),
            discord.SelectOption(label=data["dd2"]["option3"]["label3"],
                                 description=data["dd2"]["option3"]["desc3"],
                                 emoji=data["dd2"]["option3"]["emoji3"]
                                 ),
            discord.SelectOption(label=data["dd2"]["option4"]["label4"],
                                 description=data["dd2"]["option4"]["desc4"],
                                 emoji=data["dd2"]["option4"]["emoji4"]
                                 ),
        ]

        super().__init__(placeholder=self.name_placeholder,
                         min_values=1,
                         max_values=1,
                         options=options,
                         row=2)

    async def callback(self, interaction: discord.Interaction):

        user_selection.update_selection(interaction.user.id, self.name_placeholder, self.values[0])
        await interaction.response.defer()
        # await interaction.response.send_message(f"You have selected {self.values[0]}")
        await user_selection.check(interaction, self.name_placeholder, self.values[0])


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown1())
        self.add_item(Dropdown2())

    async def disable_after_timeout(self, message: discord.Message):
        """Disables the dropdown after {DROPDOWNTIMEOUT}.env seconds"""

        await asyncio.sleep(int(os.environ.get("DROPDOWNTIMEOUT")))
        for child in self.children:
            if isinstance(child, discord.ui.Select):
                child.disabled = True  # Disable dropdown
        await message.edit(view=self)  # Update message
