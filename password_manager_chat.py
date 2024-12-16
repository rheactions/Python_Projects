from cryptography.fernet import Fernet
import os


# Function to generate a key (you can do this once and save the key securely)
def generate_key():
    return Fernet.generate_key()


# Function to save the key to a file (You should only run this once and store it securely)
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# Function to load the key from the file
def load_key():
    return open("secret.key", "rb").read()


# Function to encrypt password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password


# Function to decrypt password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password


# Function to add a password for a website
def add_password(website, password, key):
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {encrypted_password.decode()}\n")


# Function to view passwords for a website
def view_password(website, key):
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            site, encrypted_pass = line.split(" | ")
            if site == website:
                decrypted_password = decrypt_password(encrypted_pass.strip().encode(), key)
                return decrypted_password
    return None


# Main function to interact with the password manager
def main():
    print("Welcome to the Password Manager")
    # Check if the key exists
    if not os.path.exists("secret.key"):
        print("No key found, generating a new key...")
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    while True:
        print("\nSelect an option:")
        print("1. Add a new password")
        print("2. View an existing password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website: ")
            password = input("Enter the password: ")
            add_password(website, password, key)
            print(f"Password for {website} has been saved.")

        elif choice == "2":
            website = input("Enter the website to view the password: ")
            password = view_password(website, key)
            if password:
                print(f"The password for {website} is: {password}")
            else:
                print("No password found for this website.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()


# How This Code Works:
# Generating a Key:
#
# The generate_key() function creates a secret key to encrypt and decrypt passwords. You only need to generate and save this key once.
# Saving and Loading the Key:
#
# The key is saved in a file called secret.key, and it's loaded whenever needed to decrypt the passwords.
# Encrypting and Decrypting Passwords:
#
# Passwords are encrypted using the Fernet symmetric encryption. This ensures that even if someone has access to the passwords.txt file, they won't be able to read the actual passwords without the key.
# Password Management:
#
# The user can add passwords with the add_password() function, which stores the encrypted password in the passwords.txt file.
# The user can view the password for a particular website with the view_password() function, which decrypts the password if it exists.
# User Interaction:
#
# The main() function provides a simple text-based interface for the user to interact with, allowing them to add new passwords or view existing ones.
# Usage:
# Run the Program: When you run this, it will check for the key. If no key exists, it will generate one and store it. The key should be kept safe.
# Add a Password: You can add a new password by selecting option 1. Enter the website name and the password, and it will be saved encrypted.
# View a Password: Select option 2 to view a password by providing the website name.
# Exit: You can exit the program by selecting option 3.
# Notes:
# Security: In a real password manager, you'd want to keep the secret.key very safe. In this code, it's stored as a file, but in production, you might want to use more secure methods like environment variables or a hardware security module (HSM).
# Password Storage: The passwords are saved in passwords.txt. It's a simple text file that contains the encrypted passwords.
# This is a basic password manager, but with this foundation, you can enhance the program by adding features like:
#
# Password strength checking
# Password generation
# Better error handling
#
#
