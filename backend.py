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

# Encrypt a file with a key
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = encrypt_message(file_data, key)
    
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Decrypt a file with a key
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = decrypt_message(encrypted_data, key)

    with open(encrypted_file_path.replace('.encrypted', '_decrypted'), 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    # Generate a key (keep it secure and share it only with authorized parties)
    secret_key = generate_key()

    # Encrypt a file with the key
    file_to_encrypt = 'example.txt'
    encrypt_file(file_to_encrypt, secret_key)

    # Decrypt the file with the key
    encrypted_file_to_decrypt = 'example.txt.encrypted'
    decrypt_file(encrypted_file_to_decrypt, secret_key)
