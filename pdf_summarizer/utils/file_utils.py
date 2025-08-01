from tkinter import filedialog

def save_summary_to_file(summary_text):
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(summary_text)
