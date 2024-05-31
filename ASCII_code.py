import tkinter as tk
from tkinter import messagebox
import time

def show_clipboard(label):
    try:
        # Get the clipboard content
        clipboard_content = root.clipboard_get()
        # Update the label with the clipboard content
        label.config(text=f"COPIED TEXT:\n{clipboard_content}")
        return clipboard_content
    except tk.TclError:
        # Handle the exception silently
        return None

def paste_text(event=None):
    try:
        # Get the clipboard content and display it as pasted text
        pasted_content = root.clipboard_get()
        pasted_text_label.config(text=f"PASTED TEXT:\n{pasted_content}")
        # Compare copied and pasted text
        copied_text = pasted_text_label.cget("text").replace("PASTED TEXT:\n", "")
        if pasted_content != copied_text:
            messagebox.showwarning("Mismatch", "COPIED TEXT and PASTED TEXT DO NOT MATCH.")
            root.deiconify()  # Show the GUI if texts don't match
    except tk.TclError:
        # Handle the exception silently
        pass

def generate_blinking_text():
    text = "Monitoring"
    while True:
        print(f"\r{text} ", end='', flush=True)  # Print the text
        time.sleep(2)  # Wait for 1 second
        print(f"\r{' ' * len(text)} ", end='', flush=True)  # Clear the text with spaces
        time.sleep(1)  # Wait for 1 second before blinking again

def check_clipboard_periodically():
    # Show the clipboard content only if there's a mismatch
    clipboard_content = show_clipboard(copied_text_label)
    if clipboard_content:
        # Compare copied and pasted text
        copied_text = pasted_text_label.cget("text").replace("PASTED TEXT:\n", "")
        if clipboard_content != copied_text:
            messagebox.showinfo("Clipboard Content", f"Clipboard Content:\n{clipboard_content}")

    # Schedule the next check
    root.after(1000, check_clipboard_periodically)  # Check every 1000 milliseconds (1 second)

def display_ascii_art():
    ascii_art = """
 ______________________________________________________|______________________
 \_______________________________________CLIPPER_GUARD_|_||_||_||_||_||_||_||_|
                                                       | 
"""
    print(ascii_art)

# Display ASCII art
display_ascii_art()

# Create the main window and hide it initially
root = tk.Tk()
root.withdraw()

# Create and place a label to show the copied text
copied_text_label = tk.Label(root, text="COPIED TEXT:\n", justify=tk.LEFT)
copied_text_label.pack(pady=20)

# Create and place a label to show the pasted text
pasted_text_label = tk.Label(root, text="PASTED TEXT:\n", justify=tk.LEFT)
pasted_text_label.pack(pady=20)

# Generate the blinking text
generate_blinking_text()

# Start checking the clipboard periodically
check_clipboard_periodically()

# Run the application
root.mainloop()
