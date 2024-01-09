URL https://desktop-fsqkmmdxhgyb9egguu6sxe.streamlit.app/
# Search Medicine US

## Dataset
Dataset yang digunakan dalam aplikasi ini adalah file CSV bernama `Medicine_Details.csv`. File ini berisi informasi tentang berbagai obat-obatan yang tersedia di Amerika Serikat. Setiap baris dalam file ini mencakup beberapa kolom yang memuat informasi seperti nama obat, kategori, deskripsi, dan lainnya.

## Permasalahan dan Tujuan
Permasalahan yang ingin diselesaikan adalah memberikan pengguna kemampuan untuk mencari informasi tentang obat-obatan yang spesifik dari dataset yang tersedia. Tujuannya adalah memberikan pengguna kemudahan dalam menemukan informasi tentang obat-obatan yang mereka cari.

## Model dan Alur Eksperimen
Aplikasi ini menggunakan konsep TF-IDF (Term Frequency-Inverse Document Frequency) untuk melakukan pencarian. Berikut adalah alur eksperimen:
1. Pemrosesan awal data: Tokenisasi, stemming, dan penggabungan kolom untuk vektorisasi TF-IDF.
2. Pembuatan model TF-IDF menggunakan `TfidfVectorizer`.
3. Penghitungan kesamaan kosinus antara query pengguna dan dokumen menggunakan matriks TF-IDF.
4. Pengurutan hasil pencarian berdasarkan kesamaan kosinus.

## Proses Deploy
Untuk menjalankan aplikasi ini, pastikan Anda memiliki Python dan pustaka yang dibutuhkan seperti `streamlit`, `pandas`, `scikit-learn`, dan `nltk`. Berikut adalah langkah-langkah untuk menjalankan aplikasi:
1. Instal semua pustaka yang dibutuhkan dengan menjalankan `pip install -r requirements.txt`.
2. Jalankan aplikasi dengan perintah `streamlit run search_medicine_us.py`.
3. Aplikasi akan dijalankan pada server lokal dan dapat diakses melalui browser dengan alamat `http://localhost:8501`.

Anda dapat memasukkan kata kunci pencarian pada antarmuka web yang akan muncul, dan aplikasi akan menampilkan hasil pencarian yang relevan berdasarkan dataset obat-obatan yang disediakan.

Happy searching!
