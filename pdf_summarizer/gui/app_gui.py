import tkinter as tk
from tkinter import filedialog, messagebox
from core.pdf_reader import extract_text_from_pdf
from core.summarizer import summarize_text
from utils.file_utils import save_summary_to_file

def start_gui():
    def upload_pdf():
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path:
            try:
                extracted = extract_text_from_pdf(path)
                input_text.delete("1.0", tk.END)
                input_text.insert(tk.END, extracted)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def summarize():
        content = input_text.get("1.0", tk.END)
        if content.strip():
            try:
                summary = summarize_text(content)
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, summary)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "No text to summarize.")

    def save_summary():
        summary = output_text.get("1.0", tk.END)
        if summary.strip():
            save_summary_to_file(summary)
            messagebox.showinfo("Success", "Summary saved.")
        else:
            messagebox.showwarning("Warning", "No summary to save.")

    root = tk.Tk()
    root.title("PDF Text Summarizer")
    root.geometry("800x600")

    tk.Button(root, text="Upload PDF", command=upload_pdf).pack(pady=10)
    tk.Label(root, text="Extracted Text:").pack()
    input_text = tk.Text(root, height=15)
    input_text.pack()

    tk.Button(root, text="Summarize", command=summarize).pack(pady=10)
    tk.Label(root, text="Summary:").pack()
    output_text = tk.Text(root, height=10)
    output_text.pack()

    tk.Button(root, text="Save Summary", command=save_summary).pack(pady=10)
    root.mainloop()
