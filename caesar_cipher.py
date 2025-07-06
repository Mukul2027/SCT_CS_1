def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            # Adjust shift for decryption
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Leave non-alphabetic characters unchanged

    return result

def main():
    print("=== Caesar Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    message = input("Enter the message: ")
    
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift value.")

    if mode == 'encrypt':
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print("Encrypted message:", encrypted)
    elif mode == 'decrypt':
        decrypted = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted message:", decrypted)
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
