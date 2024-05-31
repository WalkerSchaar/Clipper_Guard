import time
import tkinter as tk
from tkinter import messagebox
import win32clipboard

def empty_clipboard():
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
    except:
        win32clipboard.CloseClipboard()

def get_clipboard_content():
    try:
        win32clipboard.OpenClipboard()
        content = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return content
    except TypeError:
        # Handle the case where clipboard content is not text
        win32clipboard.CloseClipboard()
        return None

def check_clipboard_changes():
    previous_content = None

    while True:
        clipboard_content = get_clipboard_content()

        if clipboard_content and clipboard_content != previous_content:
            # Prompt user to confirm they have pasted the content
            print("Clipboard content detected.")
            if messagebox.askyesno("Alert", "Clipboard content detected. Have you pasted the content?"):
                empty_clipboard()
                messagebox.showinfo("Alert", "Clipboard content cleared.")
            previous_content = clipboard_content

        time.sleep(1)  # Check every second

if __name__ == "__main__":
    # Initialize tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Empty the clipboard immediately when the script starts
    empty_clipboard()
    
    check_clipboard_changes()
