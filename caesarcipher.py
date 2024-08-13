import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#determine if user encrypting or decrypting
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')


#ask the user what key value to use
while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key(0 to {maxKey} to use)')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

#fun part! ask user to input message
print(f'Please enter the message you wish to {mode}')
message = input('> ')
message = message.upper()

#lets store the encrypted/decrypted form of the message
translated_message = ''

#lets ecrypt/decrypt
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        #add ecrypted/decrypted numbers symbol to translated
        translated_message = translated_message + SYMBOLS[num]

    else:
        #just add symbol without encrypting
        translated_message = translated_message + symbol


print(translated_message)

pyperclip.copy(translated_message)
print(f'Full {mode}ed message copied to clipboard')


