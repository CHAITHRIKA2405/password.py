import random
import string


def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a random selection from all characters
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure randomness and convert to a string
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(number, length):
    return [generate_password(length) for _ in range(number)]


def main():
    # Get user input for the number of passwords and their length
    try:
        number_of_passwords = int(input("Enter the number of passwords to generate: "))
        length_of_passwords = int(input("Enter the length of each password: "))

        if length_of_passwords < 4:
            print("Password length should be at least 4 to include all character types.")
            return

        passwords = generate_passwords(number_of_passwords, length_of_passwords)
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}: {password}")
    except ValueError:
        print("Please enter valid integers for the number and length of passwords.")


if __name__ == "__main__":
    main()