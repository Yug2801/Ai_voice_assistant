import tkinter as tk
from ui import FullScreenApp

def main():
    # Create the Tkinter root window
    root = tk.Tk()

    # Provide the required arguments for FullScreenApp
    app = FullScreenApp(master=root, gif_path="gifloader.gif")

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
