
from collections import Counter
import string

def shift_text(text, shift):
    """Shift English letters while preserving case and symbols."""
    result = []

    for ch in text:
        if ch in string.ascii_uppercase:
            base = ord("A")
            result.append(chr((ord(ch) - base + shift) % 26 + base))

        elif ch in string.ascii_lowercase:
            base = ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))

        else:
            result.append(ch)

    return "".join(result)

def encrypt(text, key):
    return shift_text(text, key)

def decrypt(text, key):
    return shift_text(text, -key)

def brute_force(text):
    """Try all 26 possible shifts."""
    print("\nAll possible shifts:")

    for key in range(26):
        print(f"Shift {key:2}: {decrypt(text, key)}")

def auto_crack(text):
    """Guess the encryption key using letter frequency."""
    letters = [
        ch.lower() for ch in text
        if ch in string.ascii_letters
    ]

    if not letters:
        print("No English letters found.")
        return

    most_common = Counter(letters).most_common(1)[0][0]
    key = (ord(most_common) - ord("e")) % 26

    print(f"\nMost common letter: {most_common}")
    print(f"Guessed key: {key}")
    print("Decrypted guess:", decrypt(text, key))
    print("Note: This is only an estimate.")

def get_key():
    while True:
        try:
            key = int(input("Enter shift (1-25): "))

            if 1 <= key <= 25:
                return key

            print("Enter a number between 1 and 25.")

        except ValueError:
            print("Please enter a valid number.")

def get_message():
    while True:
        message = input("Enter message: ")

        if message.strip():
            return message

        print("Message cannot be empty.")

def main():
    print("=== Caesar Cipher Tool ===")

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Brute-force")
        print("4. Auto-crack")
        print("5. Quit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            message = get_message()
            key = get_key()
            print("Encrypted:", encrypt(message, key))

        elif choice == "2":
            message = get_message()
            key = get_key()
            print("Decrypted:", decrypt(message, key))

        elif choice == "3":
            brute_force(get_message())

        elif choice == "4":
            auto_crack(get_message())

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Select 1-5.")

if __name__ == "__main__":
    main()
