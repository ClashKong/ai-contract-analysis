# 🤖 AI-Vertragsanalyse für Banken & FinTechs

Dieses Projekt analysiert Kreditverträge mit Hilfe von Natural Language Processing (NLP), extrahiert wichtige Vertragsklauseln und bewertet das Risiko automatisch.

---

## 🚀 Features

- ✅ **PDF-Verarbeitung:** Extrahiert Text direkt aus PDF-Dateien
- ✅ **Named Entity Recognition (NER):** Erkennt Schlüsselbegriffe wie Zinssatz, Laufzeit, Vertragsstrafe u.v.m.
- ✅ **Risiko-Scoring:** Automatische Bewertung von Vertragsrisiken (0–10)
- ✅ **Modernes Frontend:** Streamlit-Oberfläche mit Emojis, Farben & UX-Feedback
- ✅ **API-Backend:** FastAPI-Schnittstellen für Text & PDF

---

## 🧠 Technologien

- **Python**  
- **spaCy** (Custom NER Modell)  
- **FastAPI** (API Backend)  
- **Streamlit** (UI)  
- **PyMuPDF & Tesseract** (PDF + OCR)  

---

## 💻 Beispiel-Request (API)

```json
POST /analyze-pdf
{
  "klauseln": {
    "ZINSSATZ": "3,5%",
    "LAUFZEIT": "10 Jahre",
    "VERTRAGSSTRAFE": "5.000 EUR"
  },
  "risiko_score": 6,
  "bewertung": "Mittel"
}
```

---

## 🖼️ Screenshots / GIFs

> Hier kannst du später ein GIF/Screenshot deiner Anwendung einfügen (z. B. mit `recordit`, `Loom`, o.ä.)

---

## 🧪 Lokale Installation & Test

```bash
git clone https://github.com/deinusername/ai-contract-analysis.git
cd ai-contract-analysis
python -m venv venv
source venv/bin/activate  # oder venv\Scripts\activate auf Windows
pip install -r requirements.txt

# Modell trainieren (optional)
python models/train_ner.py

# API starten
uvicorn api.main:app --reload

# UI starten
streamlit run frontend/app.py
```

---

## 🌍 Optionales Deployment (z. B. Hugging Face Spaces)
- [ ] Noch nicht live, aber geplant!

---

## 👨‍💻 Autor
**M.G.** – NLP & AI-Enthusiast aus Deutschland 🇩🇪, auf Mission in San Francisco 🌉

---

## 📬 Kontakt
- GitHub: [github.com/ClashKong](https://github.com/ClashKong)


