import os
from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser
import aspose.words as aw
from pdf2docx import Converter

# ------------PDF 2 WORD ------------
def convert_pdf_to_word(pdf_file, output_dir):
    try:
        if not pdf_file.endswith('.pdf'):
            raise ValueError("File is not PDF.")
       
        docx_file = os.path.join(output_dir, os.path.splitext(os.path.basename(pdf_file))[0] +'.docx')
        conv = Converter(pdf_file)
        conv.convert(docx_file, start=0, end=None)
        conv.close()

        messagebox.showinfo("Conversion Complete", f"File saved at: {docx_file}")

    except Exception as e:
        print(f"Error during conversion {e}")
        messagebox.showerror("Conversion Failed", f"Error: {e}")

# ------------------ WORD 2 PDF -----------------
def convert_word_to_pdf(docx_file, output_dir):
    try:
        if not docx_file.endswith('.docx'):
            raise ValueError("File is not DOCX.")
    
        pdf_file = os.path.join(output_dir, os.path.splitext(os.path.basename(docx_file))[0] + '.pdf')
        document = aw.Document(docx_file)
        document.save(pdf_file)
        
        messagebox.showinfo("Conversion Complete", f"File saved at: {pdf_file}")

    except Exception as e:
        print(f"Error during conversion {e}")
        messagebox.showerror("Conversion Failed", f"Error: {e}")

# --------------- START PROCESS ----------------
def process_conversion(input_file, output_dir):
    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension == '.pdf':
        convert_pdf_to_word(input_file, output_dir)
    elif file_extension == '.docx':
        convert_word_to_pdf(input_file, output_dir)
    else:
        print("Unsupported file type.")

# --------- Choose Output Directory ----------
def outputDirectory():
    selected_directory = filedialog.askdirectory(title="Select output directory")
    if selected_directory:
        messagebox.showinfo("Directory selected",f"Directory selected: {selected_directory}")
        return selected_directory
    else:
        messagebox.showwarning(title="Warning!",text="No directory has been chosen.")
        return None

# --------- Choose PDF Input --------------
def choose_pdf_file():
    selectFile = filedialog.askopenfilename(
        title = "Select a PDF file.",
        filetypes=[("PDF files", "*.pdf")]
    )
    if selectFile:
        messagebox.showinfo("File selected", f"Selected PDF: {selectFile}")
    return selectFile

# ---------- Choose DOCX, DOC Output ------------
def choose_doc_file():
    selectFile = filedialog.askopenfilename(
        title = "Select a DOC or DOCX file",
        filetypes=[("Word files","*.docx;*.doc")]
    )
    if selectFile:
        messagebox.showinfo("File selected", f"Selected Word file: {selectFile}")
    return selectFile