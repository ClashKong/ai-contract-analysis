from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import spacy
import shutil
import os
from backend.pdf_parser import extract_text_from_pdf

app = FastAPI()

# Lade das trainierte Modell
nlp = spacy.load("models/contract_ner_v2")

class ContractRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_contract(request: ContractRequest):
    """Analysiert einen Vertragstext und extrahiert Vertragsbedingungen."""
    doc = nlp(request.text)
    extracted_entities = {ent.label_: ent.text for ent in doc.ents}
    return extracted_entities

@app.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...)):
    """Nimmt eine PDF-Datei, extrahiert den Text und analysiert die Vertragsbedingungen."""
    file_path = f"temp_{file.filename}"
    
    # Speichere die Datei temporär
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Extrahiere Text aus der PDF
    text = extract_text_from_pdf(file_path)
    
    # Lösche temporäre Datei
    os.remove(file_path)
    
    # Falls kein Text gefunden wurde
    if not text.strip():
        return {"error": "Kein Text in der PDF gefunden"}
    
    # NLP-Analyse durchführen
    doc = nlp(text)
    extracted_entities = {ent.label_: ent.text for ent in doc.ents}
    
    return extracted_entities
