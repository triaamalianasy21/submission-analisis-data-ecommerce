# Proyek Analisis Data: E-Commerce Public Dataset 🛍️

## Deskripsi
Proyek ini merupakan tugas akhir dari alur belajar "Belajar Analisis Data dengan Python" di Dicoding. Proyek ini bertujuan untuk melakukan analisis mendalam terhadap dataset E-Commerce untuk menjawab pertanyaan bisnis dan memberikan insight mengenai performa penjualan serta profil pelanggan menggunakan metode **RFM (Recency, Frequency, & Monetary)**.

## Pertanyaan Bisnis
- Wilayah mana yang memiliki jumlah pelanggan terbanyak?
- Kategori produk apa yang paling diminati dan memberikan revenue tertinggi?
- Bagaimana profil loyalitas pelanggan berdasarkan analisis RFM?

## Struktur Direktori
- `dashboard/`: Berisi file dashboard interaktif (`dashboard.py`) dan data hasil olahan (`main_data.csv`).
- `data/`: Folder berisi dataset mentah (CSV) yang digunakan dalam analisis.
- `notebook.ipynb`: File dokumentasi lengkap proses wrangling, EDA, hingga visualisasi data.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.
- `url.txt`: Tautan menuju dashboard atau repository proyek.

## Instalasi
1. Clone repository ini ke komputer lokal:
   git clone [https://github.com/triaamalianasy21/submission-analisis-data-ecommerce.git](https://github.com/triaamalianasy21/submission-analisis-data-ecommerce.git)
2. Masuk ke direktori proyek
   cd submission-analisis-data-ecommerce
3. Instal library yang dibutuhkan menggunakan pip:
   pip install -r requirements.txt
4. Menjalankan Dashboard
   Untuk menjalankan dashboard Streamlit, gunakan perintah berikut di terminal:
   streamlit run dashboard/dashboard.py
