
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
    #if it has "!", change to "u"

#Asks the user to input the encrypted data

#Calling the def function to decrypt the user's input
#Print the decrypted text