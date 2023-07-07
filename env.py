import os
from dotenv import dotenv_values
from cryptography.fernet import Fernet


# Generate a key and save it to a file
key = Fernet.generate_key()


if os.path.exists("config/secret.key"):
    with open('config/secret.key', 'rb') as file:
        key = file.read()
        # Create a Fernet object with the key
        f = Fernet(key)
else:

    print("The file does not exist")
    with open('config/secret.key', 'wb') as file:
        file.write(key)

        # Load the key from the file
    with open('config/secret.key', 'rb') as file:
        key = file.read()
        # Create a Fernet object with the key
        f = Fernet(key)

 
if os.path.exists(".env.encode"):
    os.remove(".env.encode")
else:
    print("The file does not exist")
    
if os.path.exists(".env.decode"):
    os.remove(".env.decode")
else:
    print("The file does not exist")

# Load the contents of the file to encrypt
with open(".env", 'rb') as file:
    message = file.read()


# Encrypt the message
encrypted_message = f.encrypt(message)

# Save the encrypted message to a new file
with open(".env.encode", 'wb') as file:
    file.write(encrypted_message)


# Load the encrypted message from the new file
with open(".env.encode", 'rb') as file:
    encrypted_message = file.read()

# Decrypt the message
decrypted_message = f.decrypt(encrypted_message)

# Convert the decrypted bytes back into a string
print(decrypted_message.decode())

# Save the encrypted message to a new file
with open(".env.decode", 'wb') as file:
    file.write(decrypted_message)