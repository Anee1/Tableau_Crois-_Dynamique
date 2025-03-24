import streamlit as st
import pandas as pd
from pivottablejs import pivot_ui
import streamlit.components.v1 as components
import os
import io

# Configuration de la page en mode large
st.set_page_config(layout="wide")

# Titre de l'application
st.title("📊 Analyse de données avec Tableau Croisé Dynamique")

# Upload du fichier (CSV ou Excel)
uploaded_file = st.file_uploader("📂 Importer un fichier CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Détection du type de fichier et lecture
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
        df = pd.read_excel(uploaded_file, engine="openpyxl")  # Lecture du fichier Excel


        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False, encoding="utf-8")


        csv_buffer.seek(0)  # Revenir au début du buffer
        df = pd.read_csv(csv_buffer)

    # Générer le tableau croisé dynamique dans un fichier temporaire
    pivot_ui(df, outfile_path="pivot.html")

    # Lire et afficher le fichier HTML en plein écran
    with open("pivot.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        components.html(html_content, height=800, scrolling=True)

    # Supprimer le fichier temporaire après affichage
    os.remove("pivot.html")

else:
    st.info("📥 Veuillez importer un fichier CSV ou Excel pour commencer l'analyse.")


