from random import choice, randint

def valid_key_generator(key_length):
    global letters
    key = ''
    letters ="abcdefghijklmnopqrstuvwxyz"
    
    for x in range(key_length):
        key = key + choice(letters)
    
    return key

#basic caesar encrypt function
def caesar_enc(message, shift):
    encrypted_message_data = []
    encrypted_message = ''
    while shift>94:
        shift=shift-94
    
    message_data = list(message.encode('ascii'))
    
    for char in message_data:
        if char>=32 and char<=126:
            char = char + shift
            while char > 126:
                remaining_shift = char-127
                char = 32+remaining_shift
        encrypted_message_data.append(char)
        
    for enc_char in encrypted_message_data:
        encrypted_message = encrypted_message + chr(enc_char)
    return encrypted_message
#complementary caesar decrypt function 
def caesar_dec(encrypted_message, shift):
    decrypted_message_data = []
    decrypted_message = ""
    while shift > 94:
        shift = shift-94
        
    message_data = list(encrypted_message.encode('ascii'))
    
    for char in message_data:
        if char>=32 and char<=126:
            char = char - shift
            if char < 32:
                remaining_shift = 32-char
                char = 127 - remaining_shift
        decrypted_message_data.append(char)
    
    for dec_char in decrypted_message_data:
        decrypted_message = decrypted_message+chr(dec_char)
    return decrypted_message
    
def encrypt (message, key):
    #padding length is determined by the last 2 letters of the key
    pad_length_front = (ord(key[len(key)-2]) - 97)
    pad_length_rear = (ord(key[len(key)-1]) - 97)
    encrypted_message = ""
    key_index = 0
    
    pad_front = generate_random_printable(pad_length_front)
    pad_rear = generate_random_printable(pad_length_rear)
    
    encrypted_message = encrypted_message + pad_front
    
    for character in message:
        if key_index>=len(key)-2:
            key_index = 0
        #does a caesar cipher on the current char from the message, 
        #converts a letter from the key into an ascii int code for the shift
        true_char = caesar_enc(character, ord(key[key_index]))
        
        key_index = key_index+1
        if key_index>=len(key)-2:
            key_index = 0
        #uses the a random letter from the message as the character that is shifed 
        #uses the next letter in the key's ascii code as the shift
        garbage_char = caesar_enc(choice(message), ord(key[key_index]))
        key_index = key_index+1
        
        encrypted_message = encrypted_message + true_char + garbage_char 
        
    encrypted_message = encrypted_message + pad_rear
    return encrypted_message

def decrypt(enc_message, key):
    dec_message = ''
    #gets rid of garbage characters
    enc_message = garbage_collector(enc_message, pad_len_front = (ord(key[len(key)-2])-97), pad_len_rear = (ord(key[len(key)-1])-97))
    key_index = 0
    
    # increments at +2 because the encrypt function uses a new letter from the key for every character, including garbage characters
    for char in enc_message:
        if key_index>=len(key)-2:
            key_index = 0
        dec_message = dec_message + caesar_dec(char, ord(key[key_index]))
        key_index = key_index+2
    return dec_message

#removes the garbage characters at both ends and then removes the garbage characters after every true character
def garbage_collector(string,pad_len_front, pad_len_rear):
    #string indicer
    string =  string[pad_len_front:(len(string)-pad_len_rear):2]
    return string
    
  #generates random string of printable ascii characters, takes an int for length    
def generate_random_printable(length):
    printable = ''
    for x in range(length):
        letter = randint(32,126)
        printable = printable + chr(letter)
    return printable

#choice = input("> 1. Encrypt\n> 2. Decrypt\n> ")

def recursive_stupid_fuck(choice):
    if choice == "1":
        message = input("> Plaintext: ")
        key = input("> Key: ")
        print(f"> Ciphertext:\n> {encrypt(message, key)}")
    elif choice == "2":
        print("> Plaintext\n> " + decrypt(input("> Ciphertext: "), key=key))
    else:
        pass
    recursive_stupid_fuck(input("> "))

recursive_stupid_fuck(input("> 1. Encrypt\n> 2. Decrypt\n> "))   



