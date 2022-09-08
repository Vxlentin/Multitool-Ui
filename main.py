from pystyle import * 
import sys
import time
from colorama import Fore

#COLOR VARIABLE
w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX



#MAIN TEXT
print('')
print('')
Write.Print("  __  ______  __  _____    ___________  ________ \n", Colors.purple_to_blue, interval=0.0005)
Write.Print("  \ \/ / __ \/ / / / _ \  /_  __/ __/ |/_/_  __/ \n", Colors.purple_to_blue, interval=0.0005)
Write.Print("   \  / /_/ / /_/ / , _/   / / / _/_>  <  / /    \n", Colors.purple_to_blue, interval=00.005)
Write.Print("   /_/\____/\____/_/|_|   /_/ /___/_/|_| /_/     \n", Colors.purple_to_blue, interval=0.0005)
Write.Print("                                                 \n", Colors.purple_to_blue, interval=0.0005)

#YOUR MULTITOOL LIST
Write.Print("               ┌───────────────────┐", Colors.purple_to_blue, interval=0.000)
print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{lb}               │ [{w}1{Fore.RESET}{m}]{Fore.RESET} YOUR FEAUTURE{lb} │
{lb}               │ [{w}2{Fore.RESET}{m}]{Fore.RESET} YOUR FEAUTURE{lb} │
{lb}               │ [{w}3{Fore.RESET}{m}]{Fore.RESET} YOUR FEAUTURE{lb} │
{lb}               │ [{w}4{Fore.RESET}{m}]{Fore.RESET} YOUR FEAUTURE{lb} │
{lb}               │ [{w}5{Fore.WHITE}{m}]{Fore.RESET} YOUR ABOUT   {lb} │
{lb}               │ [{w}6{Fore.WHITE}{m}]{Fore.RESET} EXIT         {lb} │''')
Write.Print("               └───────────────────┘", Colors.purple_to_blue, interval=0.000)
print("")
print("")
choice = input('\x1B[1m >>\x1B[1m ')



if choice == '1':

    print("YOUR FEATURE")



if choice == '2':

    print("YOUR FEATURE")



if choice == '3':

    print("YOUR FEATURE")



if choice == '4':

    print("YOUR FEATURE")



if choice == '5':

        Write.Print("\nYOUR TEXT\nYOUR TEXT 2\nYOUR TEXT 3\nYOUR TEXT 4\n", Colors.purple_to_blue, interval=0.015)

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to EXIT: ')
      

if choice == '6':
            sys.exit(0)


