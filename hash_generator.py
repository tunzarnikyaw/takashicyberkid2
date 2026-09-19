from tkinter import *
from tkinter import ttk

import hashlib

def generate_hash():
    """Generates a SHA-256 hash for the given input text."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text_to_hash.get("1.0", END).encode('utf-8'))
    hash_output.delete("1.0", END)
    hash_output.insert("1.0", sha256_hash.hexdigest())


window = Tk()
window.title("Hash Generator")

ttk.Label(window, text="Enter text to hash:").grid(row=0, column=0, sticky=W)
text_to_hash = Text(window, width=80, height=5)
text_to_hash.grid(row=1, column=0, padx=5, pady=5)

btn_hash = ttk.Button(window, text="Generate Hash", command=generate_hash)
btn_hash.grid(row=2, column=0, pady=5)

ttk.Label(window, text="Hash Output:").grid(row=3, column=0, sticky=W)
hash_output = Text(window, width=80, height=1)
hash_output.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()