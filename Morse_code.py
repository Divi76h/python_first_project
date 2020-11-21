MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..',
                   'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-',
                   'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----',
                   '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', "'": '.---.', '"': '.-..-.',
                   '.': '.-.-.-', '!': '-.-.--', '?': '..--..',
                   '/': '-..-.', '-': '-....-', ':': '---...',
                   '=': '-...-', '+': '.-.-.', '(': '-.--.',
                   ')': '-.--.-', '&': '.-...', '@': '.--.-.'}


def encrypt():
    message = str(input("Please enter the message you want to encrypt: ")).upper

    cipher = ''

    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    print("Encrypted message:", cipher)


def decrypt():
    message = str(input("Please enter the message you want to decrypt: "))
    message += ' '

    decipher = ''
    citext = ''

    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    print("Decrypted message:", decipher)


def main():
    print("Morse Code ciphr-decipher/encryption-decryption/encode-decode\n\n"
          "Format:\n"
          ". = dot/dit\n"
          "- = dash/dah\n"
          "single space ( ) = between every character\n"
          "double space (  ) = between every word\n\n"
          "1) Cipher/Encrypt\n"
          "2) Decipher/Decrypt")

    while True:
        option = str(input("\nPlease enter your option: "))
        if option == "1":
            try:
                encrypt()
            except:
                print("Some characters you entered are not supported or not decodeable")
            break
        elif option == "2":
            try:
                decrypt()
            except:
                print("The message you want to decrypt is not in the right format or "
                      "some characters are not supported or not decodeable")
            break
        else:
            print("Wrong Input!")


if __name__ == '__main__':
    main()
