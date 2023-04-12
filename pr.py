import random
import string
import time
import colorama
from colorama import Fore, Style, Back

pushvalue = 1

print(Fore.GREEN + "Initiating..." + Style.RESET_ALL)
time.sleep(1)

if pushvalue == 1:
    print("Checking validation")
    # define the possible characters for the string
    characters = string.ascii_letters + string.digits

    # generate a random 6-character string
    random_string = ''.join(random.choices(characters, k=6))
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{random_string}")