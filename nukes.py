#skidsec practice coding
#nukes

import colorama
import time
from colorama import Fore, Back, Style
print("""

___  ________ _____ _____ _____ _      _____   _   _ _   _ _   __ _____ _____ 
|  \/  |_   _/  ___/  ___|_   _| |    |  ___| | \ | | | | | | / /|  ___/  ___|
| .  . | | | \ `--.\ `--.  | | | |    | |__   |  \| | | | | |/ / | |__ \ `--. 
| |\/| | | |  `--. \`--. \ | | | |    |  __|  | . ` | | | |    \ |  __| `--. \
| |  | |_| |_/\__/ /\__/ /_| |_| |____| |___  | |\  | |_| | |\  \| |___/\__/ /
\_|  |_/\___/\____/\____/ \___/\_____/\____/  \_| \_/\___/\_| \_/\____/\____/ 
                                                                              
                                                                              

""")
print("thank you for using our tool\n")
print("if you want to message me here is my contact number and fb account")
print("contact me: 09272881510")
print("facebook: ian narito\n")
print(Fore.RED + 'please be careful using our tool, it may be become a real thing:)')

num = input("how many missile do you want to use?\n")
print(num)

print("type the coordinates")
lat = input("\nLatitude: ")
print(lat)

long = input("\nLongitude: ")
print(long)

print("\ncalculating coordinates\n")
time.sleep(5)
print("Encrypting missiles to prevent getting track")
time.sleep(5)

def print_format_table():
    """
    prints table of formatted text format options
    """

    for style in range(30):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


print_format_table()

time.sleep(2)
print("preparing missiles to get launch\n")
time.sleep(5)
print("5 seconds is enough to launch the missile\n")


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
time.sleep(3)
print("""
   _____  ____   ____  _____     _____ _    _  ____ _______  
  / ____|/ __ \ / __ \|  __ \   / ____| |  | |/ __ \__   __| 
 | |  __| |  | | |  | | |  | | | (___ | |__| | |  | | | |    
 | | |_ | |  | | |  | | |  | |  \___ \|  __  | |  | | | |    
 | |__| | |__| | |__| | |__| |  ____) | |  | | |__| | | |    
  \_____|\____/ \____/|_____/  |_____/|_|  |_|\____/  |_|    
                                                             
                                                             
""")
