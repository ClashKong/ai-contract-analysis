from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# API starten
app = FastAPI()

# Lade das neue trainierte Modell
nlp = spacy.load("models/contract_ner_v2")

# Pydantic Schema für API-Anfragen
class ContractRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_contract(request: ContractRequest):
    """Analysiert einen Vertragstext und extrahiert Vertragsbedingungen."""
    doc = nlp(request.text)
    extracted_entities = {ent.label_: ent.text for ent in doc.ents}
    return extracted_entities
