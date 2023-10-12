import customtkinter
import tkinter as tk
import cv2
from PIL import Image, ImageTk

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

        self.camera = cv2.VideoCapture(0)  # 0 for default camera

        self.update_camera()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_center = (screen_width - 1300) // 2
        y_center = (screen_height - 700) // 2
        self.root.geometry(f"1300x700+{x_center}+{y_center}")

    def create_widgets(self):
        frame = customtkinter.CTkFrame(master=self.root, width=150, height=40)
        frame.pack_propagate(False)
        frame.place(relx=0.82, rely=0.125, anchor=tk.W)

        label = customtkinter.CTkLabel(master=frame, text="Player 2 ", font=("Helvetica", 19))
        label.pack(pady=9)

        frame = customtkinter.CTkFrame(master=self.root, width=150, height=40)
        frame.pack_propagate(False)
        frame.place(relx=0.175, rely=0.125, anchor=tk.E)
        
        label = customtkinter.CTkLabel(master=frame, text="Player 1 ", font=("Helvetica", 19))
        label.pack(pady=9)

        frame = customtkinter.CTkFrame(master=self.root, width=450, height=400)
        frame.pack_propagate(False)
        frame.place(relx=0.6, rely=0.45, anchor=tk.W)
        #Here is needed to be introduced the players 

        frame = customtkinter.CTkFrame(master=self.root, width=450, height=400)
        frame.pack_propagate(False)
        frame.place(relx=0.4, rely=0.45, anchor=tk.E)

        # Create a canvas to display the camera feed
        self.camera_canvas = customtkinter.CTkCanvas(self.root, width=640, height=480)
        self.camera_canvas.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Create a canvas to display the camera feed
        #self.camera_canvas = customtkinter.CTkCanvas(self.root, width=640, height=480)
       # self.camera_canvas.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Load and display the actor images on the frames
        actor_image = Image.open("Actor.png")
        actor1_image = Image.open("Actor1.jpg")

        actor_image = actor_image.resize((450, 400))
        actor1_image = actor1_image.resize((450, 400))

        self.actor_image = ImageTk.PhotoImage(actor_image)
        self.actor1_image = ImageTk.PhotoImage(actor1_image)

        # Display actor image on the left frame
        self.camera_canvas.create_image(0, 0, anchor=tk.NW, image=self.actor_image)

        # Display actor1 image on the right frame
        self.camera_canvas.create_image(640, 0, anchor=tk.NE, image=self.actor1_image)

    def update_camera(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.flip(frame, 1)

            # Convert the frame to RGB format for tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_tk = ImageTk.PhotoImage(image=frame_pil)

            # Update the camera canvas with the new frame
            self.camera_canvas.create_image(0, 0, anchor=tk.NW, image=frame_tk)
            self.camera_canvas.image = frame_tk  # Keep a reference to prevent garbage collection

        # Schedule the next update
        self.root.after(10, self.update_camera)

    def create_health_bar_LEFT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=670, height=50)
        canvas.place(relx=0.4, rely=0.08, anchor=tk.E)

        current_health = 60
        total_health = 100

        health_ratio = (current_health / total_health)
        green_width = int(health_ratio * 670)

        canvas.create_rectangle(670, 50, 0, 0, fill="#444444")
        canvas.create_rectangle(670, 50, green_width, 0, fill="#EA8E19")

    def create_health_bar_RIGHT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=670, height=50)
        canvas.place(relx=0.6, rely=0.08, anchor=tk.W)

        current_health = 90
        total_health = 100

        health_ratio = current_health / total_health
        green_width = int(health_ratio * 670)

        canvas.create_rectangle(0, 0, green_width, 50, fill="#EA8E19")
        canvas.create_rectangle(green_width, 0, 670, 50, fill="#444444")
    def create_power_bar_RIGHT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=335, height=30)
        canvas.place(relx=0.6, rely=0.1215, anchor=tk.W)

        current_health = 60
        total_health = 100

        health_ratio = current_health / total_health
        green_width = int(health_ratio * 335)

        canvas.create_rectangle(0, 0, green_width, 30, fill="#35EF26")
        canvas.create_rectangle(green_width, 0, 335, 30, fill="#444444")
    def create_power_bar_LEFT(self):
        canvas = customtkinter.CTkCanvas(self.root, width=335, height=30)
        canvas.place(relx=0.4, rely=0.1215, anchor=tk.E)

        current_health = 60
        total_health = 100

        health_ratio = current_health / total_health
        green_width = int(health_ratio * 335)

        # Create rectangles to represent power
        canvas.create_rectangle(335, 30, 0, 0, fill="#444444")
        canvas.create_rectangle(335, 30, green_width, 0, fill="#35EF26")

if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    app = App(root)
    root.mainloop()
