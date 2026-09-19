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

btn_encrypt = ttk.Button(frame1, text="Encrypt")
btn_encrypt.grid(row=3, column=0, pady=5)

btn_decrypt = ttk.Button(frame2, text="Decrypt")
btn_decrypt.grid(row=3, column=0, pady=5)

window.mainloop()