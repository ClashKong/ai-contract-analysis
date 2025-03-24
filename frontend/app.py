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
    response = None

    try:
        if uploaded_file is not None:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(API_PDF_URL, files=files)
        elif contract_text:
            data = {"text": contract_text}
            response = requests.post(API_TEXT_URL, json=data)
        else:
            st.warning("⚠️ Bitte lade eine PDF hoch oder gib einen Text ein!")

        if response and response.status_code == 200:
            result = response.json()
            print("📌 API RESPONSE IM FRONTEND:", result)  # Debugging

            st.success("✅ Analyse abgeschlossen! Hier sind die Vertragsklauseln:")

            klauseln = result.get("klauseln", {})
            for label, value in klauseln.items():
                if isinstance(value, list):
                    value = ", ".join(value)
                st.markdown(f"### 📌 **{label}:** `{value}`")

            st.markdown("---")
            st.subheader("🧠 Vertrags-Risikoanalyse:")

            score = result.get("risiko_score", 0)
            bewertung = result.get("bewertung", "Unbekannt")

            # Bewertung visuell aufbereiten
            if score <= 3:
                farbe = "🟢"
                emoji = "✅"
            elif score <= 6:
                farbe = "🟡"
                emoji = "⚠️"
            else:
                farbe = "🔴"
                emoji = "🚨"

            st.metric("🔢 Risiko-Score", f"{score} / 10", help="Je höher der Score, desto riskanter der Vertrag.")
            st.markdown(f"### {emoji} **Bewertung:** {farbe} **{bewertung} Risiko**")

            if score >= 7:
                st.warning("🚨 Achtung: Dieser Vertrag enthält mehrere Risikofaktoren. Prüfe die Klauseln genau.")
            elif score <= 3:
                st.success("✅ Gute Nachricht: Der Vertrag wirkt insgesamt risikoarm.")
            else:
                st.info("ℹ️ Dieser Vertrag enthält gemischte Risikomerkmale.")

        else:
            st.error("❌ Fehler bei der Analyse. Bitte versuche es erneut!")
            print("⚠️ Fehler in API-Antwort:", response.text if response else "Keine Antwort")

    except Exception as e:
        st.error(f"🚨 Fehler: {str(e)}")
        print("🚨 Ausnahme aufgetreten:", str(e))

st.write("---")
st.write("🚀 Entwickelt von M.G. für AI-gestützte Vertragsanalyse.")
