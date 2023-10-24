import customtkinter
import tkinter as tk
from SignIn import Signin


class LoginApp:
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


    def sign_in(self):
        # Add code to handle the sign-in process when the "Sign In" button is clicked
        # You can open a new window or navigate to a sign-in page here
        print("Sign In button clicked")

    def create_widgets(self):
        frame = customtkinter.CTkFrame(master=self.root, width=450, height=500)
        frame.pack_propagate(False)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = customtkinter.CTkLabel(master=frame, text="Hi! Please choose an option to login",
                                       font=("Arial Greek", 20))
        label.pack(pady=25)

        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", font=("Arial", 20))
        entry1.pack(pady=12, padx=10)

        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", font=("Arial", 20))
        entry2.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=frame, text="Login", command=self.login, font=("Arial", 20, "bold"),
                                         fg_color="#E88655", hover_color="#EBA17C")
        button.pack(pady=12, padx=10)

        anonymous = customtkinter.CTkButton(master=frame, text="Anonymous", command=self.enter_anonymous,
                                            font=("Arial", 20, "bold"), fg_color="#2190C7", hover_color="#5BB2DE")
        anonymous.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me", font=("Arial", 20), fg_color="#E88655",
                                             hover_color="#EBA17C")
        checkbox.pack(pady=12, padx=10)

        # Add a label above the "Sign In" button
        label_dont_have_account = customtkinter.CTkLabel(master=frame, text="Don't have an account yet?",
                                                         font=("Arial", 14))
        label_dont_have_account.pack(pady=10)

        # Add a "Sign In" button below the label
        sign_in_button = customtkinter.CTkButton(master=frame, text="Sign In", command=self.open_signin_page,
                                                 font=("Arial", 20, "bold"), fg_color="#E88655", hover_color="#EBA17C")
        sign_in_button.pack(pady=5)  # Specify a smaller pady value to keep the button visible

    def open_signin_page(self):
        self.root.destroy()  # Close the current LoginApp window
        root = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        app = Signin(root)
        root.mainloop()


if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    app = LoginApp(root)
    root.mainloop()