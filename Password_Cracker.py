from random import *

print('  /$$$$$$  /$$$$$$$\   /$$     /$$  /$$$$$$$   /$$$$$$$$  /$$$$$$         /$$$$$$  /$$   /$$ /$$$$$$$$')
print(' /$$__  $$| $$__  $$  |  $$   /$$/ | $$__  $$ |__  $$__/ /$$__  $$       /$$__  $$| $$  | $$|__  $$__/')
print('| $$  \__/| $$  \ $$   \  $$ /$$/  | $$  \ $$    | $$   | $$  \ $$      | $$  \ $$| $$  | $$   | $$')
print('| $$      | $$$$$$$/    \  $$$$/   | $$$$$$$/    | $$   | $$  | $$      | $$  | $$| $$  | $$   | $$')
print('| $$      | $$__  $$     \  $$/    | $$____/     | $$   | $$  | $$      | $$  | $$| $$  | $$   | $$')
print('| $$    $$| $$  \ $$      | $$     | $$          | $$   | $$  | $$      | $$  | $$| $$  | $$   | $$')
print('|  $$$$$$/| $$  | $$      | $$     | $$          | $$   |  $$$$$$/      |  $$$$$$/|  $$$$$$/   | $$')
print(' \______/ |__/  |__/      |__/     |__/          |__/    \______/        \______/  \______/    |__/')
print('                                                    VERSION 1.0                                     ')
print('------------------------------------///////////////////////-----------------------------------------')
print('                                     CODED BY     SARVESH                                              ')
usr_pass= input('[+] Enter Your Password : ')
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess = ""

while (guess != usr_pass):
    guess = ""
    for word in range(len(usr_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
        print(guess)
print('[+] PASSWORD CRACKED, PASSWORD IS ' + guess)
print('[+] HAPPY HACKING')
