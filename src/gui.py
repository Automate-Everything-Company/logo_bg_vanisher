from pathlib import Path
from tkinter import filedialog
from tkinter import Tk


def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a folder
    folder_path = Path(filedialog.askdirectory(initialdir=Path.cwd(), title="Select Folder"))
    return folder_path
