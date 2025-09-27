# main.py
from tkinter import Tk
from gui import StudentGUI

if __name__ == "__main__":
    # Create the main window
    root = Tk()

    # Create an instance of the StudentGUI class
    app = StudentGUI(root)

    # Start the Tkinter event loop
    root.mainloop()