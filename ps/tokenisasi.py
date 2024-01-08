import streamlit as st
import pandas as pd

# Membaca data dari file CSV ke dalam DataFrame
data = pd.read_csv(r'desktop-tutorial/ps/Medicine_Details.csv')

# Fungsi untuk melakukan pencarian kata yang cocok secara eksak di dalam DataFrame
def exact_match_search(query):
    results = pd.DataFrame(columns=data.columns)  # DataFrame kosong untuk menyimpan hasil pencarian
    
    # Pencarian kata yang cocok secara eksak
    for column in data.columns:
        results = pd.concat([results, data[data[column].astype(str).str.lower() == query.lower()]])
    
    return results.drop_duplicates()

# Tampilan antarmuka web menggunakan Streamlit
st.title('Search Engine medicine')

# Input query dari pengguna
query = st.text_input('Masukkan kata kunci pencarian:', '')

# Pencarian saat tombol ditekan
if st.button('Cari'):
    # Hasil pencarian
    results = exact_match_search(query)
    # Menampilkan hasil pencarian ke dalam tabel
    st.write("Hasil Pencarian:")
    st.write(results)
