import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path):
    """Versucht, den Text aus einer PDF-Datei zu extrahieren."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            # Versuche, Text normal zu extrahieren
            page = doc[page_num]
            page_text = page.get_text("text")

            if page_text.strip():  # Falls normaler Text gefunden wurde
                text += page_text + "\n"
            else:
                print(f"⚠️ Seite {page_num + 1}: Kein maschinenlesbarer Text gefunden, OCR wird versucht...")
                # OCR als Backup nutzen
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes("ppm")))
                ocr_text = pytesseract.image_to_string(img)
                text += ocr_text + "\n"

    except Exception as e:
        print(f"Fehler beim Verarbeiten der PDF: {e}")

    print("📌 EXTRAHIERTER TEXT:\n", text)  # Debugging
    return text

# TESTLAUF
if __name__ == "__main__":
    extract_text_from_pdf("Testvertrag.pdf")
