import string

def separate_and_convert(string):
    # Initialize empty substrings for numbers and letters
    number_substring = ''
    letter_substring = ''
    
    # Separate numbers and letters
    for char in string:
        if char.isdigit():
            number_substring += char
        elif char.isalpha():
            letter_substring += char

    print(f"Number Substring: {number_substring}")
    print(f"Letter Substring: {letter_substring}")
    
    # Convert even numbers to ASCII decimal values
    even_numbers_ascii = [ord(num) for num in number_substring if int(num) % 2 == 0]
    
    # Convert uppercase letters to ASCII decimal values
    uppercase_letters_ascii = [ord(letter) for letter in letter_substring if letter.isupper()]

    print("\nASCII Decimal Values of Even Numbers in Number Substring:")
    print(even_numbers_ascii)

    print("\nASCII Decimal Values of Upper-case Letters in Letter Substring:")
    print(uppercase_letters_ascii)

# Test the function with an example string
test_string = "56aAww1984sktr23527aYmn145ss785fsq31D0"
separate_and_convert(test_string)
    
# Decrypt the cryptogram by shifting each letter by the shift_key value

def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_message = ""
    
    # Decrypt the cryptogram by shifting each letter by the shift_key value
    for char in cryptogram:
        if char.isalpha():
            if char.isupper():
                # Uppercase letters: ord('A') = 65, shift within A-Z
                decrypted_message += chr((ord(char) - shift_key - 65) % 26 + 65)
            else:
                # Lowercase letters: ord('a') = 97, shift within a-z
                decrypted_message += chr((ord(char) - shift_key - 97) % 26 + 97)
        else:
            # Keep spaces and punctuation unchanged
            decrypted_message += char
    
    return decrypted_message
 
def shift_key(cryptogram):
        shift_key = 13
        decrypted_message = decrypt_cryptogram(cryptogram, shift_key)
        print(f"Shift key {shift_key}: {decrypted_message}")

# Example cryptogram (this is what we are trying to decrypt)
cryptogram = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V 
NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ BG UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA 
LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

# Step 4: Decrypt the cryptogram with all possible shift keys
shift_key(cryptogram)