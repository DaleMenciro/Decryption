
import colorama
from colorama import Fore,Style

#Code Starts


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
#Calling the def function to decrypt the user's input
decrypted_data= decrypt_data(encrypted_data)

#Print the decrypted text