from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())  # your fernet_key, keep it in secured place! 

#example = GkRnVIdmuf5QEA4XBWbyeUB7P0vFEzDEm7llz-ul2R8=