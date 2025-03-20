import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Vertragsanalyse", layout="wide")

st.title("📄 AI-gestützte Vertragsanalyse")
st.write("Lade einen Vertrag als **PDF** oder **Text** hoch, und unser NLP-Modell analysiert ihn!")

uploaded_file = st.file_uploader("Wähle eine PDF-Datei aus", type=["pdf"])

contract_text = st.text_area("Oder gib einen Vertragstext manuell ein:")

API_TEXT_URL = "http://127.0.0.1:8000/analyze"
API_PDF_URL = "http://127.0.0.1:8000/analyze-pdf"

if st.button("🔍 Vertrag analysieren"):
    if uploaded_file is not None:
        
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_PDF_URL, files=files)
    elif contract_text:
        
        data = {"text": contract_text}
        response = requests.post(API_TEXT_URL, json=data)
    else:
        st.warning("Bitte lade eine PDF hoch oder gib einen Text ein!")
        response = None

    if response and response.status_code == 200:
        result = response.json()
        st.success("Analyse abgeschlossen! Hier sind die Vertragsklauseln:")
        
       
        for label, value in result.items():
            st.markdown(f"**{label}:** `{value}`")
    else:
        st.error("Fehler bei der Analyse. Bitte versuche es erneut!")


st.write("---")
st.write("🚀 Entwickelt von M.G. für AI-gestützte Vertragsanalyse.")
