import streamlit as st
import pandas as pd

# Konfiguracja strony (musi być pierwszym poleceniem Streamlit)
st.set_page_config(page_title="Alzheimer DGE Dashboard", layout="wide")

# Tytuł i opis aplikacji
st.title("🧬 Analiza transkryptomiczna: Alzheimer vs Grupa Kontrolna")
st.markdown("""
Ta aplikacja prezentuje wyniki analizy różnicowej ekspresji genów (DGE) 
na podstawie danych RNA-Seq (Zbiór GSE203206).
""")

# Funkcja do wczytywania danych (z cacheowaniem, żeby aplikacja działała błyskawicznie)
@st.cache_data
def load_data():
    # Wczytujemy nasz przygotowany wcześniej plik
    df = pd.read_csv('data/processed/deseq2_results_annotated.csv', index_col=0)
    return df

# Wczytanie danych
try:
    results_df = load_data()
    st.success(f"Pomyślnie wczytano dane dla {results_df.shape[0]} genów!")
    
    # Wyświetlamy surową tabelę z wynikami
    st.subheader("Tabela wyników DGE")
    st.dataframe(results_df)

except FileNotFoundError:
    st.error("Nie znaleziono pliku z wynikami. Upewnij się, że uruchomiłeś skrypty analityczne.")