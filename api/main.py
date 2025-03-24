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

def berechne_risiko_score(entities):
    score = 0
    text_map = {label.upper(): value for label, value in entities.items()}

    # Zinssatz prüfen
    zinssatz = text_map.get("ZINSSATZ", "")
    if "%" in zinssatz:
        try:
            zahl = float(zinssatz.replace("%", "").replace(",", "."))
            if zahl > 5:
                score += 3
        except:
            pass

    # Laufzeit prüfen
    laufzeit = text_map.get("LAUFZEIT", "")
    if "Jahr" in laufzeit:
        try:
            zahl = int("".join(filter(str.isdigit, laufzeit)))
            if zahl > 10:
                score += 2
        except:
            pass

    # Vertragsstrafe vorhanden
    if "VERTRAGSSTRAFE" in text_map:
        score += 2

    # Kündigungsfrist prüfen
    kuendigung = text_map.get("KÜNDIGUNGSFRIST", "")
    if "Monat" in kuendigung:
        try:
            zahl = int("".join(filter(str.isdigit, kuendigung)))
            if zahl > 6:
                score += 1
        except:
            pass

    # Sonderklausel positiv werten
    if "SONDERKLAUSEL" in text_map:
        score -= 1

    score = max(0, min(score, 10))
    level = "Niedrig" if score <= 3 else "Mittel" if score <= 6 else "Hoch"
    return {"risiko_score": score, "bewertung": level}

@app.post("/analyze")
def analyze_contract(request: ContractRequest):
    """Analysiert einen Vertragstext und extrahiert Vertragsbedingungen."""
    doc = nlp(request.text)
    extracted_entities = {ent.label_: ent.text for ent in doc.ents}
    risiko = berechne_risiko_score(extracted_entities)
    return {"klauseln": extracted_entities, **risiko}

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
    risiko = berechne_risiko_score(extracted_entities)

    return {"klauseln": extracted_entities, **risiko}