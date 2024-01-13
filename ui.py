import tkinter as tk
from PIL import Image, ImageTk
import imageio

class FullScreenApp:
    def __init__(self, master, gif_path):
        self.master = master
        self.master.title("Fullscreen GIF App")
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.configure(bg="black")

        self.gif_path = gif_path
        self.gif_label = None
        self.gif_frames = self.load_gif()

        self.setup_gui()

    def load_gif(self):
        gif = imageio.mimread(self.gif_path)
        frames = [Image.fromarray(img) for img in gif]
        return frames

    def setup_gui(self):
        self.current_frame = 0
        self.total_frames = len(self.gif_frames)

        # Set highlightthickness and bd to 0 to remove the border
        self.gif_label = tk.Label(self.master, bg="black", highlightthickness=0, bd=0)
        self.gif_label.pack(expand=True)

        self.update_gif()

        self.master.after(100, self.animate_gif)

    def update_gif(self):
        frame_image = ImageTk.PhotoImage(self.gif_frames[self.current_frame])
        self.gif_label.config(image=frame_image)
        self.gif_label.image = frame_image

    def animate_gif(self):
        self.current_frame = (self.current_frame + 1) % self.total_frames
        self.update_gif()
        self.master.after(100, self.animate_gif)
