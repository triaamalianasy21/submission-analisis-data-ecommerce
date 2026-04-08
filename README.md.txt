# Proyek Analisis Data: E-Commerce Public Dataset 

## Deskripsi
Proyek ini merupakan tugas akhir dari alur belajar "Belajar Fundamental Analisis Data" di Dicoding. Proyek ini bertujuan untuk melakukan analisis mendalam terhadap dataset E-Commerce untuk menjawab pertanyaan bisnis dan memberikan insight mengenai performa penjualan serta profil pelanggan menggunakan metode RFM (Recency, Frequency, & Monetary).

## Pertanyaan Bisnis
1. Kategori produk apa yang paling banyak terjual?
2. Bagaimana tren penjualan dari waktu ke waktu?

## Struktur Direktori
dashboard/: Berisi file dashboard interaktif (dashboard.py) dan data hasil olahan (main_data.csv).
data/: Folder berisi dataset mentah (CSV) yang digunakan dalam analisis.
notebook.ipynb: File dokumentasi lengkap proses wrangling, EDA, hingga visualisasi data.
requirements.txt: Daftar library Python yang dibutuhkan untuk menjalankan proyek.
url.txt: Tautan menuju repository GitHub.

## Instalasi
1. Clone repository ini ke komputer lokal:
git clone [https://github.com/triaamalianasy21/submission-analisis-data-ecommerce.git](https://github.com/triaamalianasy21/submission-analisis-data-ecommerce.git)
2. Masuk ke direktori proyek:
   ```
   cd submission-analisis-data-ecommerce
   ```
4. Instal library yang dibutuhkan menggunakan pip:
   ```
   pip install -r requirements.txt
   ```
6. Menjalankan Dashboard
   Untuk menjalankan dashboard Streamlit, gunakan perintah berikut di terminal:
   ```
   streamlit run dashboard/dashboard.py
   ```

## Kesimpulan
  Pertanyaan 1: Kategori produk bed_bath_table menjadi yang utama dengan penjualan tertinggi, disusul oleh health_beauty. Ini menunjukkan kategori kebutuhan rumah tangga dan   perawatan diri memiliki permintaan yang tinggi.
  Pertanyaan 2: Penjualan menunjukkan tren pertumbuhan yang positif sejak awal 2017, dengan lonjakan drastis pada November 2017, membuktikan efektivitas kampanye pemasaran     pada periode tersebut.
  Analisis Lanjutan (RFM): Sebagian besar pelanggan saat ini adalah pembeli baru (high recency) namun masih bersifat one-time buyer (low frequency), yang menjadi peluang       untuk program retensi pelanggan.

Nama: Tria Amalia Anasya
ID Dicoding: CDCC409D6X2388
