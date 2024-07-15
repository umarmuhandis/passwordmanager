import random
import re
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Password Manager")

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(row=0, column=0, columnspan=3, pady=10)

original_image = Image.open("logo.png")
resized_image = original_image.resize((300, 300), Image.LANCZOS)
logo = ImageTk.PhotoImage(resized_image)

canvas.create_image(150, 150, image=logo)

website_label = tk.Label(root, text="Website:")
website_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
website_entry = tk.Entry(root, width=35)
website_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="w")

email_label = tk.Label(root, text="Email / Username:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=35)
email_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="w")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, width=21)
password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")


def generate_password():
  characters = string.ascii_letters + string.digits + string.punctuation
  password_length = 12
  password = ''.join(random.choice(characters) for i in range(password_length))
  password_entry.delete(0, tk.END)
  password_entry.insert(0, password)


generate_button = tk.Button(root,
                            text="Generate Password",
                            command=generate_password)
generate_button.grid(row=3, column=2, padx=(5, 10), pady=5, sticky="w")


def save_to_file():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()

  url_regex = re.compile(
      r'^(https?:\/\/)?([a-z0-9-]+\.)+[a-z]{2,6}(\/.*)*\/?$')

  if not website or not email or not password:
    messagebox.showwarning(title="Warning",
                           message="Please fill out all fields.")
    return

  if not url_regex.match(website):
    messagebox.showwarning(title="Invalid URL",
                           message="Please enter a valid URL.")
    return

  with open("data.txt", "a") as file:
    file.write(f"Website: {website} | Email: {email} | Password: {password}\n")

  messagebox.showinfo(title="Success", message="Data saved successfully!")
  website_entry.delete(0, tk.END)
  email_entry.delete(0, tk.END)
  password_entry.delete(0, tk.END)


add_button = tk.Button(root, text="Add", width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2, pady=10)
root.mainloop()
