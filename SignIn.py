import customtkinter
import tkinter as tk
import re
import sqlite3
import hashlib
from dataManager import DatabaseHandler


class Signin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700")
        self.center_window()
        self.root.configure(bg="#99CCFF")
        self.checkbox_state = tk.BooleanVar()

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

    def show_message_popup(self, message):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Message")

        # Create a dark mode theme
        popup_window.configure(bg="#333333")

        popup_label = tk.Label(popup_window, text=message, fg="white", bg="#333333",
                               font=("Arial", 16))  # Adjust the font size as needed
        popup_label.pack(pady=20)

        close_button = tk.Button(popup_window, text="OK", command=popup_window.destroy, bg="#E88655", fg="white",
                                 font=("Arial", 16))  # Adjust the font size as needed
        close_button.pack()

        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the pop-up window
        popup_width = 400  # Adjust the width
        popup_height = 150  # Adjust the height
        x_center = (screen_width - popup_width) // 2
        y_center = (screen_height - popup_height) // 2

        # Set the position and dimensions of the pop-up window to center it
        popup_window.geometry(f"{popup_width}x{popup_height}+{x_center}+{y_center}")

    def create_widgets(self):
        frame = customtkinter.CTkFrame(master=self.root, width=450, height=500)
        frame.pack_propagate(False)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = customtkinter.CTkLabel(master=frame, text="Create an Account", font=("Arial Greek", 30))
        label.pack(pady=25)

        self.first_name_entry = customtkinter.CTkEntry(master=frame, placeholder_text="First Name", font=("Arial", 20),
                                                       width=200)
        self.first_name_entry.pack(pady=12, padx=10)

        self.last_name_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Last Name", font=("Arial", 20),
                                                      width=200)
        self.last_name_entry.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username", font=("Arial", 20),
                                                     width=200)
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*",
                                                     font=("Arial", 20), width=200)
        self.password_entry.pack(pady=12, padx=10)

        self.email_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Email", font=("Arial", 20), width=200)
        self.email_entry.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=frame, text="Create Account", command=self.create_account,
                                         font=("Arial", 20, "bold"), fg_color="#E88655", hover_color="#EBA17C", width=170)
        button.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions",
                                             font=("Arial", 20), fg_color="#E88655", hover_color="#EBA17C",
                                             variable=self.checkbox_state)
        checkbox.pack(pady=12, padx=10)

    @staticmethod
    def is_valid_name(name):
        return bool(re.match("^[A-Za-z]+$", name))

    def create_account(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()

        if not self.is_valid_name(first_name):
            self.show_message_popup("Invalid first name. Please use only letters.")
            return

        if not self.is_valid_name(last_name):
            self.show_message_popup("Invalid last name. Please use only letters.")
            return

        if self.checkbox_state.get():
            self.login()
        else:
            self.show_message_popup("Please agree to the terms and conditions.")


if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    app = Signin(root)
    root.mainloop()
