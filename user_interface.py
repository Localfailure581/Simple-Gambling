import os
import random
from simple_gambling import roll, flip, betflip, betroll

if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Interface:
    def __init__(self):
        self.commands = ["roll", "flip", "betflip", "betroll", "exit"]
        self.current_command = ""
        self.gamble_amount = ""

    def print_header(self):
        print(f"{Color.BOLD}{Color.BLUE}\n" +
              "╔════════════════════════════════════╗\n" +
              "║           Simple Gambling           ║\n" +
              "╚════════════════════════════════════╝\n" +
              f"{Color.ENDC}")

    def get_user_command(self):
        self.current_command = input(f"{Color.BOLD}{Color.GREEN}What function would you like to use? " +
                                     f"(Type '{Color.RED}exit{Color.GREEN}' to quit){Color.ENDC} ")
        print()

    def handle_command(self):
        if self.current_command not in self.commands:
            valid_commands = ", ".join(self.commands)
            print(f"{Color.WARNING}Invalid command. Please use one of the following: {valid_commands}.{Color.ENDC}\n")
            return

        if self.current_command == "exit":
            print(f"{Color.GREEN}Thank you for using Simple Gambling!{Color.ENDC}")
            exit()

        if self.current_command == "roll":
            roll()

        if self.current_command == "flip":
            flip()

        if self.current_command == "betflip":
            betflip()

        if self.current_command == "betroll":
            betroll()

    def run(self):
        self.print_header()

        while True:
            self.get_user_command()
            self.handle_command()


if __name__ == "__main__":
    interface = Interface()
    interface.run()