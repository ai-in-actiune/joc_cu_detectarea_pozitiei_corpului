import customtkinter
import tkinter as tk
import sqlite3
import hashlib
from database import DatabaseHandler

class Signin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700")
        self.center_window()
        self.root.configure(bg="#99CCFF")

        self.create_widgets()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_center = (screen_width - 1300) // 2
        y_center = (screen_height - 700) // 2
        self.root.geometry(f"1300x700+{x_center}+{y_center}")

    def login(self):
        print("test")

    def enter_anonymous(self):
        print("test_anonymous")

    def create_widgets(self):
        frame = customtkinter.CTkFrame(master=self.root, width=450, height=400)
        frame.pack_propagate(False)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = customtkinter.CTkLabel(master=frame, text="Create an Account", font=("Arial Greek", 20))
        label.pack(pady=25)

        self.first_name_entry = customtkinter.CTkEntry(master=frame, placeholder_text="First Name", font=("Arial", 20))
        self.first_name_entry.pack(pady=12, padx=10)

        self.last_name_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Last Name", font=("Arial", 20))
        self.last_name_entry.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username", font=("Arial", 20))
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*",
                                                     font=("Arial", 20))
        self.password_entry.pack(pady=12, padx=10)

        self.email_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Email", font=("Arial", 20))
        self.email_entry.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=frame, text="Create Account", command=self.create_account,
                                         font=("Arial", 20, "bold"), fg_color="#E88655", hover_color="#EBA17C")
        button.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions",
                                             font=("Arial", 20), fg_color="#E88655", hover_color="#EBA17C")
        checkbox.pack(pady=12, padx=10)

    def create_account(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # Use the database handler to create the user account
        DatabaseHandler.connect()
        DatabaseHandler.create_user(first_name, last_name, username, password, email)
        DatabaseHandler.disconnect()

        print("Account created successfully!")

if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    app = Signin(root)
    root.mainloop()
