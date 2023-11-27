from flask import Flask, render_template
from encryption_utils import generate_key, encrypt_message, decrypt_message, generate_random_password

app = Flask(__name__, template_folder='templates')

# Generate a key (keep it secure and share it only with authorized parties)
secret_key = generate_key()

@app.route('/')
def index():
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

    return render_template('cyber.html', original_message=original_message,
                           encrypted_message=encrypted_message, decrypted_message=decrypted_message,
                           random_password=random_password)

if __name__ == '__main__':
    app.run(debug=True)
