from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet
import secrets

app = Flask(__name__)

# Global variable to store the encryption key (in a real-world scenario, you would store this securely)
secret_key = None

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    global secret_key
    original_message = request.form['message']

    # Check if a key has been generated
    if secret_key is None:
        secret_key = generate_key()

    # Encrypt the message
    encrypted_message = encrypt_message(original_message, secret_key)
    return render_template('result.html', result=encrypted_message)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    global secret_key
    encrypted_message = request.form['message']

    # Check if a key has been generated
    if secret_key is None:
        return "Error: No key available. Please encrypt a message first."

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message.encode(), secret_key)
    return render_template('result.html', result=decrypted_message)

@app.route('/generate_password')
def generate_password():
    random_password = generate_random_password()
    return render_template('result.html', result=random_password)

if __name__ == '__main__':
    app.run(debug=True)
