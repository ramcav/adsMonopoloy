import os
import platform


def clear_screen():
    # Check if the operating system is Windows
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
