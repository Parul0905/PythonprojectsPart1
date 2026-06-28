def encrypt(message,key):
    result=""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted=(ord(char)-start+key)%26 + start
            result+=chr(shifted)
        else:
            result+=char
    return result

def decrypt(message,key):
    return encrypt(message,-key)

choice=input('Do u want to encrypt or decrypt your message(E/D): ').strip().lower()
if choice=='e':
    text=input('Enter your message: ')
    try:
        key=int(input('Enter a number bw 1 and 25: '))
        encrypted=encrypt(text,key)
        print("Encrypted message:")
        print(encrypted)
    except ValueError as e:
        print('Invalid Key')
elif choice=='d':
    text=input('Enter your encrypted message: ')
    try:
        key=int(input('Enter a number bw 1 and 25: '))
        decrypted=decrypt(text,key)
        print("Decrypted message: ")
        print(decrypted)
    except ValueError as e:
        print('Invalid Key')
else:
    print('Enter valid choice.')