import json

with open("json/dropdown.json", "r") as file:
    data = json.load(file)

class Userselection:
    """Class to track user selections and check conditions"""

    def __init__(self):
        self.user_selections = {}  # Store user choices

    def update_selection(self, user_id, placeholder, option):
        """Update the user's selection based on the dropdown."""

        if user_id not in self.user_selections:
            self.user_selections[user_id] = {}
        self.user_selections[user_id][placeholder] = option

    async def check(self, interaction, placeholder, option):
        """Checks what user selected and sends the corresponding content."""

        user_id = interaction.user.id
        selection = self.user_selections.get(user_id, {})

        if selection.get(placeholder) == option:
            # Determine which dropdown was used
            if placeholder == data["dd1"]["placeholder"]:
                # Find the corresponding content in dd1
                for key, value in data["dd1"].items():
                    if key.startswith("option") and value.get(f"label{key[-1]}") == option:
                        content = value.get(f"content{key[-1]}")
                        await interaction.followup.send(content)
                        break
            elif placeholder == data["dd2"]["placeholder"]:
                # Find the corresponding content in dd2
                for key, value in data["dd2"].items():
                    if key.startswith("option") and value.get(f"label{key[-1]}") == option:
                        content = value.get(f"content{key[-1]}")
                        await interaction.followup.send(content)
                        break