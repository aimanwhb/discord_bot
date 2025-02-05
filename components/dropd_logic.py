
class Userselection:
    """Class to track user selections and check conditions"""

    def __init__(self):
        self.user_selections = {}  # Store user choices

    def update_selection(self, user_id, key, value):
        """Update the user's selection based on the dropdown."""
        if user_id not in self.user_selections:
            self.user_selections[user_id] = {}
        self.user_selections[user_id][key] = value

    async def check(self, interaction):
        """Checks what user selected ."""
        user_id = interaction.user.id
        selection = self.user_selections.get(user_id, {})

        if selection.get("Discord Bot") == "README":
            await interaction.followup.send("Hello!")