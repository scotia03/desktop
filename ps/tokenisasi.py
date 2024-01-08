import streamlit as st
from pathlib import Path
import pandas as pd

# Define the file path using pathlib
file_path = Path('/C/pyhton/ps/honda_sell_data.csv')

# Read the CSV file
data = pd.read_csv(file_path)

# Fungsi untuk melakukan pencarian kata yang cocok secara eksak di dalam DataFrame
def exact_match_search(query):
    results = pd.DataFrame(columns=data.columns)  # DataFrame kosong untuk menyimpan hasil pencarian
    
    # Pencarian kata yang cocok secara eksak
    for column in data.columns:
        results = pd.concat([results, data[data[column].astype(str).str.lower() == query.lower()]])
    
    return results.drop_duplicates()

# Tampilan antarmuka web menggunakan Streamlit
st.title('Search Engine Otomotif')

# Input query dari pengguna
query = st.text_input('Masukkan kata kunci pencarian:', '')

# Pencarian saat tombol ditekan
if st.button('Cari'):
    # Hasil pencarian
    results = exact_match_search(query)
    # Menampilkan hasil pencarian ke dalam tabel
    st.write("Hasil Pencarian:")
    st.write(results)
