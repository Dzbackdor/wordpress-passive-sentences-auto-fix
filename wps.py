import re
from colorama import Fore, init
import os

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
H = Fore.BLACK
Y = Fore.YELLOW

def clear_screen():
    # Mengecek sistem operasi
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def benner():
    print(f"""
{W}V.0.1{Y} {R}| {W}Dzone{B}             __                                                            
 _      ______  _________/ /___  ________  __________                                   
| | /| / / __ \/ ___/ __  / __ \/ ___/ _ \/ ___/ ___/                                   
| |/ |/ / /_/ / /  / /_/ / /_/ / /  /  __(__  |__  )                                    
|__/|__/\____/_/   \__,_/ .___/_/   \___/____/____/{W}        __                           
    ____  ____ ________{B}/_/{W}(_)   _____     ________  ____  / /____  ____  ________  _____
   / __ \/ __ `/ ___/ ___/ / | / / _ \   / ___/ _ \/ __ \/ __/ _ \/ __ \/ ___/ _ \/ ___/
  / /_/ / /_/ (__  |__  ) /| |/ /  __/  (__  )  __/ / / / /_/  __/ / / / /__/  __(__  ) 
 / .___/\__,_/____/____/_/ |___/\___/  /____/\___/_/ /_/\__/\___/_/ /_/\___/\___/____/  
/_/                                                                                                                                                                                                                            
\n""")

clear_screen()

benner()
def add_space_for_di(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    parts = re.split(r'(<[^>]+>)', content)
    updated_content = []
    for part in parts:
        if part.startswith('<') and part.endswith('>'):
            updated_content.append(part)
        else:
            part = re.sub(r'\b(di)([a-zA-Z])', r'\1 \2', part)
            updated_content.append(part)
    result = ''.join(updated_content)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(result)

    print(f"{G}repaired successfully  {W}{filename}")
    
add_space_for_di('file.txt')