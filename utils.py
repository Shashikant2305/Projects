# --- utils.py ---
# Helper functions for file handling and UI interactivity

from tkinter import filedialog
import customtkinter as ctk

recent_files = []

def browse_file(file_entry):
    path = filedialog.askopenfilename()
    if path:
        file_entry.set(path)
        update_recent_files(file_entry, path)

def update_recent_files(file_entry, path):
    if path not in recent_files:
        recent_files.insert(0, path)
        file_entry.configure(values=recent_files)
