from tkinter import *
from tkinter import ttk

# AI CODES

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(string_key: str, salt: bytes) -> bytes:
    """Derives a secure 256-bit key from a string password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes = 256 bits
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(string_key.encode('utf-8'))

def encrypt_message(message: str, string_key: str) -> tuple[bytes, bytes, bytes]:
    """Encrypts a string message using AES-256-GCM."""
    # Generate random unique salt and nonce (Initialization Vector)
    salt = os.urandom(16)
    nonce = os.urandom(12)
    
    # Derive the 256-bit binary key from the string key
    key = derive_key(string_key, salt)
    
    # Encrypt the plaintext
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, message.encode('utf-8'), None)
    
    # You must store or transmit the salt and nonce alongside the ciphertext
    return ciphertext, salt, nonce

def decrypt_message(ciphertext: bytes, string_key: str, salt: bytes, nonce: bytes) -> str:
    """Decrypts the ciphertext back into a string message."""
    # Derive the exact same key using the same salt and password
    key = derive_key(string_key, salt)
    
    # Decrypt and decode back to a string
    aesgcm = AESGCM(key)
    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted_bytes.decode('utf-8')

# End of AI CODES

def encrypt_button_clicked():
    print("Encrypt button clicked")
    print(text_to_encrypt.get("1.0", END).strip())
    print(chk_encrypt.instate(['selected']))
    print(secret_key.get("1.0", END).strip())

def decrypt_button_clicked():
    print("Decrypt button clicked")
    print(text_to_decrypt.get("1.0", END).strip())
    print(chk_decrypt.instate(['selected']))
    print(secret_key_decrypt.get("1.0", END).strip())

def copy_encrypted():
    print("Copy encrypted text")
    print(encrypted_text.get("1.0", END).strip())

def copy_decrypted():
    print("Copy decrypted text")
    print(decrypted_text.get("1.0", END).strip())

window = Tk()
window.title("Encrypt/Decrypt")

frame = ttk.Frame(window, padding=10)
frame.grid()

frame1 = ttk.LabelFrame(frame, text="Encrypt", padding=10)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = ttk.LabelFrame(frame, text="Decrypt", padding=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame1, text="Enter text to encrypt:").grid(row=0, column=0, sticky=W)
ttk.Label(frame2, text="Enter text to decrypt:").grid(row=0, column=0, sticky=W)

text_to_encrypt = Text(frame1, width=30, height=5)
text_to_encrypt.grid(row=1, column=0, padx=5, pady=5)

text_to_decrypt = Text(frame2, width=30, height=5)
text_to_decrypt.grid(row=1, column=0, padx=5, pady=5)

chk_encrypt = ttk.Checkbutton(frame1, text="Encrypt")
chk_encrypt.grid(row=2, column=0, sticky=W)

chk_decrypt = ttk.Checkbutton(frame2, text="Decrypt")
chk_decrypt.grid(row=2, column=0, sticky=W)

ttk.Label(frame1, text="Enter secret key:").grid(row=4, column=0, sticky=W)
secret_key = Text(frame1, width=30, height=1)
secret_key.grid(row=5, column=0, padx=5, pady=5)

ttk.Label(frame2, text="Enter secret key:").grid(row=4, column=0, sticky=W)
secret_key_decrypt = Text(frame2, width=30, height=1)
secret_key_decrypt.grid(row=5, column=0, padx=5, pady=5)

btn_encrypt = ttk.Button(frame1, text="Encrypt", command=encrypt_button_clicked)
btn_encrypt.grid(row=6, column=0, pady=5)

btn_decrypt = ttk.Button(frame2, text="Decrypt", command=decrypt_button_clicked)
btn_decrypt.grid(row=6, column=0, pady=5)

frame3 = ttk.LabelFrame(frame, text="Encrypted Output", padding=10)
frame3.grid(row=7, column=0, padx=10, pady=10)

frame4 = ttk.LabelFrame(frame, text="Decrypted Output", padding=10)
frame4.grid(row=7, column=1, padx=10, pady=10)

encrypted_text = Text(frame3, width=30, height=5)
encrypted_text.grid(row=0, column=0, padx=5, pady=5)

decrypted_text = Text(frame4, width=30, height=5)
decrypted_text.grid(row=0, column=0, padx=5, pady=5)

btn_copy_encrypted = ttk.Button(frame3, text="Copy", command=copy_encrypted)
btn_copy_encrypted.grid(row=1, column=0, pady=5)

btn_copy_decrypted = ttk.Button(frame4, text="Copy", command=copy_decrypted)
btn_copy_decrypted.grid(row=1, column=0, pady=5)

window.mainloop()