class Donation:
    def __init__(self):
        self.discord = "https://discord.gg/Cathie02"
        self.patreon = "https://www.patreon.com/Cathie02"

    def display(self):
        print(
            "\n==========================================\n"
            "If you like this project, consider joining\n"
            "my Discord server or support me on Patreon\n\n"
            f"  Discord: {self.discord}   \n"
            f"Patreon: {self.patreon}\n"
            "==========================================\n"
        )
