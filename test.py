import time
import threading
import tkinter as tk
from tkinter import messagebox
import win32clipboard
import pyperclip
import keyboard
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QClipboard

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

class ClipboardWatcher(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.clipboard = self.clipboard()
        self.clipboard.dataChanged.connect(self.clipboard_changed)
        self.previous_clipboard_content = ''

    def clipboard_changed(self):
        clipboard_content = self.clipboard.text()
        if clipboard_content and self.previous_clipboard_content and clipboard_content != self.previous_clipboard_content:
            # Create a top-level window to make the message box always on top
            alert_root = tk.Toplevel()
            alert_root.withdraw()  # Hide the top-level window
            alert_root.attributes('-topmost', True)  # Make it always on top
            alert_root.after(0, lambda: alert_root.focus_force())  # Force focus to this window

            messagebox.showinfo('Clipboard Alert', f'Clipboard content changed to: {clipboard_content}', parent=alert_root)
            alert_root.destroy()  # Destroy the top-level window after the message box is closed
            
            # Reset to the beginning
            self.quit()  # Quit the QApplication event loop to restart

        # Update previous clipboard content
        self.previous_clipboard_content = clipboard_content

def generate_blinking_text():
    text = "Monitoring"
    while True:
        print(f"\r{text} ", end='', flush=True)  # Print the text
        time.sleep(2)  # Wait for 2 seconds
        print(f"\r{' ' * len(text)} ", end='', flush=True)  # Clear the text with spaces
        time.sleep(1)  # Wait for 1 second before blinking again

def clear_clipboard():
    # Clear the clipboard after paste
    pyperclip.copy("")

def main():
    display_ascii_art()

    # Initialize tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Empty the clipboard immediately when the script starts
    empty_clipboard()

    # Start the blinking text in a separate thread
    blinking_thread = threading.Thread(target=generate_blinking_text)
    blinking_thread.daemon = True
    blinking_thread.start()

    # Start checking the clipboard changes using PyQt5
    app = ClipboardWatcher([])

    # Run the application
    app.exec_()  # Start the QApplication event loop

if __name__ == "__main__":
    # Detect the paste command (Ctrl+V) and clear clipboard
    keyboard.add_hotkey('ctrl+v', clear_clipboard)

    # Run the main loop
    while True:
        main()  # Restart the entire process
