from cryptography.fernet import Fernet
import secrets

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a message using a key
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Decrypt a message using a key
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate a random password
def generate_random_password(length=12):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Example usage
if_name_ == "_main_":
    # Generate a key (keep it secure and share it only with authorized parties)
    secret_key = generate_key()

    # Message to be encrypted
    original_message = "This is a secret message."

    # Encrypt the message
    encrypted_message = encrypt_message(original_message, secret_key)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, secret_key)
    print("Decrypted Message:", decrypted_message)

    # Generate a random password
    random_password = generate_random_password()
    print("Random Password:", random_password)