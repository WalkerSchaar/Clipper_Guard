import time
import threading
import tkinter as tk
from tkinter import messagebox
import win32clipboard

def display_ascii_art():
    ascii_art = """
 ______________________________________________________|______________________
 \_______________________________________CLIPPER_GUARD_|_||_||_||_||_||_||_||_|
                                                       | 
"""
    print(ascii_art)

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
        win32clipboard.CloseClipboard()
        return None

def check_clipboard_changes():
    previous_content = None

    def clipboard_check():
        nonlocal previous_content
        clipboard_content = get_clipboard_content()

        if clipboard_content and clipboard_content != previous_content:
            print("Clipboard content detected.")
            if messagebox.askyesno("Alert", "Clipboard content detected. Have you pasted the content?"):
                empty_clipboard()
                messagebox.showinfo("Alert", "Clipboard content cleared.")
            previous_content = clipboard_content

        root.after(1000, clipboard_check)  # Check every second

    clipboard_check()

def generate_blinking_text():
    text = "Monitoring"
    while True:
        print(f"\r{text} ", end='', flush=True)  # Print the text
        time.sleep(2)  # Wait for 2 seconds
        print(f"\r{' ' * len(text)} ", end='', flush=True)  # Clear the text with spaces
        time.sleep(1)  # Wait for 1 second before blinking again

if __name__ == "__main__":
    display_ascii_art()

    # Initialize tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Empty the clipboard immediately when the script starts
    empty_clipboard()

    # Start checking the clipboard changes
    check_clipboard_changes()

    # Start the blinking text in a separate thread
    blinking_thread = threading.Thread(target=generate_blinking_text)
    blinking_thread.daemon = True
    blinking_thread.start()

    # Run the application
    root.mainloop()
