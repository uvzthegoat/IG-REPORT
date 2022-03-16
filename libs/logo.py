# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
    _                                     __     __          __ 
   (_)___ _   ________  ____  ____  _____/ /_   / /_  ____  / /_
  / / __ `/  / ___/ _ \/ __ \/ __ \/ ___/ __/  / __ \/ __ \/ __/
 / / /_/ /  / /  /  __/ /_/ / /_/ / /  / /_   / /_/ / /_/ / /_  
/_/\__, /  /_/   \___/ .___/\____/_/   \__/  /_.___/\____/\__/  
  /____/            /_/                                         
                             
                                            """



def print_logo():
    print(Fore.MAGENTA + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")

    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
