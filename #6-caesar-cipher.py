"""
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.
"""

"""
In modern times, the Caesar cipher isn’t very sophisticated, but that 
makes it ideal for beginners. The program in Project 7, “Caesar Hacker,” 
can brute-force through all 26 possible keys to decrypt messages, even if 
you don’t know the original key. Also, if you encrypt the message with the 
key 13, the Caesar cipher becomes identical to Project 61, “ROT 13 Cipher.” 

Learn more about the Caesar cipher at https://en.wikipedia.org/wiki/Caesar_
cipher. If you’d like to learn about ciphers and code breaking in general, you 
can read my book Cracking Codes with Python (No Starch Press, 2018; https://
nostarch.com/crackingcodes/).
"""

from email import message


try:
    import pyperclip
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True:
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = input("> ")
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d.")


# Let the user enter the key to use:
while True:
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input("> ").upper()

    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break


# Let the user enter the message to encrypt/decrypt:
print("Enter the message to {}".format(mode))
message = input("> ")

# Cesar cipher only works on uppercase letters:
message = message.upper()

# Stores the encrypt/decrypt form of the message:
translated = ""

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol) # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        

        # Handle the wrap-around if num is larger than the length of  SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol



print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed.








"""
IMPORTED FUNCTIONS

.startswith()
.isdeciaml()
"""