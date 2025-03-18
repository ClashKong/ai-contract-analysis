📁 AI-Contract-Analysis/
│-- backend/  # Enthält API-Logik (FastAPI)
│-- models/  # Enthält NLP-Modelle & Trainingsscripte
│-- api/  # API-Endpunkte
│-- tests/  # Tests für die API und NLP-Modelle
│-- data/  # Trainings- und Testdaten
│-- .gitignore  # Vermeidung unnötiger Dateien im Repo
│-- requirements.txt  # Liste benötigter Python-Packages
│-- README.md  # Projektbeschreibung

# .gitignore (Basis für Python-Projekte)
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env
*.log

# requirements.txt (Grundlegende Abhängigkeiten)
fastapi
uvicorn
spacy
torch
tensorflow
transformers
pandas
scikit-learn

# README.md (Initialer Inhalt)
# AI-gestützte Vertragsanalyse für Banken

## 🚀 Projektbeschreibung
Dieses Projekt analysiert Kreditverträge mit NLP, um Banken zu unterstützen.

### 🔹 Features:
- **Automatische Extraktion von Kreditbedingungen** (Named Entity Recognition)
- **Erkennung von Risikobegriffen** in Verträgen
- **Echtzeit-API** für Vertragsbewertung

### 🔧 Technologien:
- **Python, FastAPI, spaCy, BERT, GPT**
- **Machine Learning & NLP**

### 📌 Setup
1. **Repo klonen:** `git clone <repo-url>`
2. **Virtuelle Umgebung erstellen:** `python -m venv venv`
3. **Abhängigkeiten installieren:** `pip install -r requirements.txt`
4. **API starten:** `uvicorn api.main:app --reload`

### 🏆 Zielgruppe
- Banken & FinTechs mit Fokus auf NLP
- ML-Ingenieure & Data Scientists, die sich mit NLP beschäftigen
