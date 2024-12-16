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
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def benner():
    print(f"""
{W}V.1.1{Y} {R}| {W}Dzone{B}             __                                                            
 _      ______  _________/ /___  ________  __________                                   
| | /| / / __ \/ ___/ __  / __ \/ ___/ _ \/ ___/ ___/                                   
| |/ |/ / /_/ / /  / /_/ / /_/ / /  /  __(__  |__  )                                    
|__/|__/\____/_/   \__,_/ .___/_/   \___/____/____/{W}        __                           
    ____  ____ ________{B}/_/{W}(_)   _____     ________  ____  / /____  ____  ________  _____
   / __ \/ __ `/ ___/ ___/ / | / / _ \   / ___/ _ \/ __ \/ __/ _ \/ __ \/ ___/ _ \/ ___/
  / /_/ / /_/ (__  |__  ) /| |/ /  __/  (__  )  __/ / / / /_/  __/ / / / /__/  __(__  ) 
 / .___/\__,_/____/____/_/ |___/\___/  /____/\___/_/ /_/\__/\___/_/ /_/\___/\___/____/  
/_/   {W}++ {Y}checker {G}<{W}h2{G}>{R} | {G}<{W}h3{G}>{R} | {G}<{W}h4{G}>                                                                                                                                                                                                                       
""")
clear_screen()
benner()
def check_headings_in_order(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    headings = re.findall(r'<(h[2-4])[^>]*>(.*?)</\1>', content)

    found_h2 = False
    found_h3 = False
    found_h4 = False
    if headings:
        print(f"Headings {G}found {W}in the file :")
        for tag, heading in headings:
            print(f"{G}<{W}{tag}{G}>{Y}{heading}{G}</{W}{tag}{G}>")
            if tag == 'h2':
                found_h2 = True
            elif tag == 'h3':
                found_h3 = True
            elif tag == 'h4':
                found_h4 = True
    if not found_h2:
        print(f"\n{R}Error {W}: {R}<{W}h2{R}> {W}tag {R}not found{W}.")
    if not found_h3:
        print(f"\n{R}Error {W}: {R}<{W}h3{R}> {W}tag {R}not found{W}.")
    if not found_h4:
        print(f"\n{R}Error {W}: {R}<{W}h4{R}> {W}tag {R}not found{W}.")
def add_space_for_di_and_check_headings(filename):
    check_headings_in_order(filename)

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

    print(f"\n{G}The content of the file {W}{filename} {G}has been successfully updated{W}.")
add_space_for_di_and_check_headings('file.txt')
