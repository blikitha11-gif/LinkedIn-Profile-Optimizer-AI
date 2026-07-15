import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""

    # Open PDF
    document = fitz.open(pdf_path)

    # Read every page
    for page in document:
        text += page.get_text()

    document.close()

    return text