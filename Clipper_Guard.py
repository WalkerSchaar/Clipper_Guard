import tkinter as tk
from tkinter import messagebox

def show_clipboard():
    try:
        # Get the clipboard content
        clipboard_content = root.clipboard_get()
        # Update the label with the clipboard content
        copied_text_label.config(text=f"COPIED TEXT:\n{clipboard_content}")
    except tk.TclError:
        
def paste_text(event=None):
    try:
        # Get the clipboard content and display it as pasted text
        pasted_content = root.clipboard_get()
        pasted_text_label.config(text=f"PASTED TEXT:\n{pasted_content}")
        # Compare copied and pasted text
        copied_text = copied_text_label.cget("text").replace("COPIED TEXT:\n", "")
        if pasted_content != copied_text:
            messagebox.showwarning("Mismatch", "COPIED TEXT and PASTED TEXT DO NOT MATCH.")
    except tk.TclError:
        # If clipboard is empty or there's an error, show a different message
        pasted_text_label.config(text="PASTED TEXT:\nClipboard is empty or contains unsupported content")

def display_ascii_art():
    ascii_art = """
 ______________________________________________________|______________________
 \_______________________________________CLIPPER_GUARD_|_||_||_||_||_||_||_||_|
                                                       | 
"""
    print(ascii_art)

# Display ASCII art
display_ascii_art()

# Create the main window
root = tk.Tk()
root.title("Clipboard Viewer")

# Create and place a button that triggers the show_clipboard function
button = tk.Button(root, text="Show Clipboard", command=show_clipboard)
button.pack(pady=20)

# Create and place a label to show the copied text
copied_text_label = tk.Label(root, text="COPIED TEXT:\n", justify=tk.LEFT)
copied_text_label.pack(pady=20)

# Create and place a label to show the pasted text
pasted_text_label = tk.Label(root, text="PASTED TEXT:\n", justify=tk.LEFT)
pasted_text_label.pack(pady=20)

# Bind the paste event to the paste_text function
root.bind('<Control-v>', paste_text)
root.bind('<Command-v>', paste_text)  # For macOS

# Run the application
root.mainloop() 
