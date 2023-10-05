import customtkinter
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700")
        self.center_window()
        self.root.configure(bg="#99CCFF")
        self.create_widgets()
        self.create_health_bar_LEFT()
        self.create_health_bar_RIGHT()
        self.create_power_bar_RIGHT()
        self.create_power_bar_LEFT()

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
        frame = customtkinter.CTkFrame(master=self.root, width=200, height=50)
        frame.pack_propagate(False)
        frame.place(relx=0.7, rely=0.85, anchor=tk.W)

        label = customtkinter.CTkLabel(master=frame, text="Player 2 ", font=("Arial Greek", 25))
        label.pack(pady=10)

        frame = customtkinter.CTkFrame(master=self.root, width=200, height=50)
        frame.pack_propagate(False)
        frame.place(relx=0.3, rely=0.85, anchor=tk.E)
        
        label = customtkinter.CTkLabel(master=frame, text="Player 1 ", font=("Arial Greek", 25))
        label.pack(pady=10)

        frame = customtkinter.CTkFrame(master=self.root, width=450, height=400)
        frame.pack_propagate(False)
        frame.place(relx=0.6, rely=0.5, anchor=tk.W)
        #Here is needed to be introduced the players 

        frame = customtkinter.CTkFrame(master=self.root, width=450, height=400)
        frame.pack_propagate(False)
        frame.place(relx=0.4, rely=0.5, anchor=tk.E)

    def create_health_bar_LEFT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=670, height=50)
        canvas.place(relx=0.4, rely=0.1, anchor=tk.E)

        current_health = 10
        total_health = 100

        health_ratio = current_health / total_health
        green_width = int(health_ratio * 670)

        canvas.create_rectangle(0, 0, green_width, 50, fill="#EA8E19")
        canvas.create_rectangle(green_width, 0, 670, 50, fill="#444444")

    def create_health_bar_RIGHT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=670, height=50)
        canvas.place(relx=0.6, rely=0.1, anchor=tk.W)

        current_health = 90
        total_health = 100

        health_ratio = current_health / total_health
        green_width = int(health_ratio * 670)

        canvas.create_rectangle(0, 0, green_width, 50, fill="#EA8E19")
        canvas.create_rectangle(green_width, 0, 670, 50, fill="#444444")

    def create_power_bar_RIGHT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=670, height=30)
        canvas.place(relx=0.6, rely=0.14, anchor=tk.W)
        current_health = 30
        total_health = 100
        health_ratio = current_health / total_health
        green_width = int(health_ratio * 670)
        canvas.create_rectangle(0, 0, green_width, 30, fill="#35EF26")
        canvas.create_rectangle(green_width, 0, 670, 30, fill="#444444")

    def create_power_bar_LEFT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=670, height=30)
        canvas.place(relx=0.4, rely=0.14, anchor=tk.E)
        current_health = 60
        total_health = 100
        health_ratio = current_health / total_health
        green_width = int(health_ratio * 670)

        # Create rectangles to represent health
        canvas.create_rectangle(0, 0, green_width, 30, fill="#35EF26")
        canvas.create_rectangle(green_width, 0, 670, 30, fill="#444444")
     

if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    app = App(root)
    root.mainloop()
