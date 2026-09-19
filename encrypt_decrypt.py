from tkinter import *
from tkinter import ttk

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

btn_encrypt = ttk.Button(frame1, text="Encrypt")
btn_encrypt.grid(row=6, column=0, pady=5)

btn_decrypt = ttk.Button(frame2, text="Decrypt")
btn_decrypt.grid(row=6, column=0, pady=5)

frame3 = ttk.LabelFrame(frame, text="Encrypted Output", padding=10)
frame3.grid(row=7, column=0, padx=10, pady=10)

frame4 = ttk.LabelFrame(frame, text="Decrypted Output", padding=10)
frame4.grid(row=7, column=1, padx=10, pady=10)

encrypted_text = Text(frame3, width=30, height=5)
encrypted_text.grid(row=0, column=0, padx=5, pady=5)

decrypted_text = Text(frame4, width=30, height=5)
decrypted_text.grid(row=0, column=0, padx=5, pady=5)

btn_copy_encrypted = ttk.Button(frame3, text="Copy")
btn_copy_encrypted.grid(row=1, column=0, pady=5)

btn_copy_decrypted = ttk.Button(frame4, text="Copy")
btn_copy_decrypted.grid(row=1, column=0, pady=5)

window.mainloop()