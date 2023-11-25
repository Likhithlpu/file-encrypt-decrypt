from cryptography.fernet import Fernet
import secrets

def generate_key():
    return Fernet.generate_key()


def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

def generate_random_password(length=12):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    secret_key = generate_key()

    original_message = "This is a secret message."

    encrypted_message = encrypt_message(original_message, secret_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, secret_key)
    print("Decrypted Message:", decrypted_message)

    random_password = generate_random_password()
    print("Random Password:", random_password)