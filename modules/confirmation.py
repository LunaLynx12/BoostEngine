class Confirmation:
    def __init__(self):
        self.warning = "This action might create instability in your system. Do you want to continue? (y/n): "

    def ask(self):
        if input(self.warning).strip().lower() == "y":
            #continue the process
            pass
        else:
            print("Operation aborted.")
            exit(0)