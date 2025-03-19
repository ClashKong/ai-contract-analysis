import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extrahiert den Text aus einer PDF-Datei."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Fehler beim Verarbeiten der PDF: {e}")
    return text
