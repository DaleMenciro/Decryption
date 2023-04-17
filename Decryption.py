
import colorama
from colorama import Fore,Style

#Code Starts
print(Style.BRIGHT + Fore.CYAN + u"\u2500" * 50 )
print(Fore.BLACK + Style.RESET_ALL + "Welcome to Problem 2".center(50," "))
print(Style.BRIGHT + Fore.CYAN + u"\u2500" * 50, end="\n\n" )
import time
time.sleep(1)

#Def function for the conditions in decrypting
def decrypt_data(encrypted_data):
    #if it has "*", change to "a"
    decrypted_data= encrypted_data.replace("*",Fore.BLUE +"a"+ Style.RESET_ALL)
    #if it has "&", change to "e"
    decrypted_data= decrypted_data.replace("&",Fore.GREEN +"e"+ Style.RESET_ALL)
    #if it has "#", change to "i"
    decrypted_data= decrypted_data.replace("#",Fore.MAGENTA +"i"+ Style.RESET_ALL)
    #if it has "+", change to "o"
    decrypted_data= decrypted_data.replace("+",Fore.RED +"o"+ Style.RESET_ALL)
    #if it has "!", change to "u"
    decrypted_data= decrypted_data.replace("!",Fore.YELLOW +"u"+ Style.RESET_ALL)
    return decrypted_data


#Asks the user to input the encrypted data
print(Style.DIM + Fore.LIGHTGREEN_EX + u"\u2500" * 50)
encrypted_data= input(Style.BRIGHT + Fore.MAGENTA + "Kindly enter your encrypted data: ")
print(Style.DIM + Fore.LIGHTGREEN_EX + u"\u2500" * 50, end= "\n ")
print(Fore.GREEN + Style.NORMAL + "You entered:",encrypted_data)
print(Style.DIM + Fore.LIGHTGREEN_EX + u"\u2500" * 50 + Style.RESET_ALL, end= "\n ")
time.sleep (0.5)

print(Style.NORMAL + Fore.YELLOW + u"\u2500" * 50,end="\n\n")

from tqdm import tqdm
import time

#Calling the def function to decrypt the user's input
decrypted_data= decrypt_data(encrypted_data)

print("The Program is Decrypting your data.....")
for i in tqdm(range(10)):
    time.sleep(0.5)
print(Fore.CYAN + "Done!\n\n" + Style.RESET_ALL)

#Print the decrypted text
print(Style.DIM + Fore.LIGHTGREEN_EX + u"\u2500" * 50)
print(Style.RESET_ALL + "Your Decrypted Text is:", decrypted_data )
print(Style.DIM + Fore.LIGHTGREEN_EX + u"\u2500" * 50)