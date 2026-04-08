import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur tampilan visual 
sns.set(style='whitegrid')

# ==========================================
# 1. LOAD DATA
# ==========================================
df = pd.read_csv("main_data.csv")

# ==========================================
# 2. SIDEBAR 
# ==========================================
with st.sidebar:
    st.title("Analisis Pelanggan 📊")
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    st.write("### Tentang Project")
    st.info("Dashboard ini dibuat untuk melihat profil pelanggan E-Commerce berdasarkan seberapa baru, seberapa sering, dan seberapa banyak mereka belanja (Metode RFM).")
    
    st.write("### Profil Pengembang")
    st.write("- **Nama:** Tria Amalia Anasya")
    st.write("- **ID Dicoding:** CDCC409D6X2388")

# ==========================================
# 3. MAIN PAGE 
# ==========================================
st.header('Dashboard Analisis Pelanggan (RFM) 🛍️')

# Menampilkan ringkasan data (Metrics)
col1, col2, col3 = st.columns(3)
with col1:
    avg_recency = round(df.recency.mean(), 1)
    st.metric("Rata-rata Terakhir Belanja", value=f"{avg_recency} Hari")

with col2:
    avg_frequency = round(df.frequency.mean(), 2)
    st.metric("Rata-rata Jumlah Transaksi", value=f"{avg_frequency} Kali")

with col3:
    avg_monetary = round(df.monetary.mean(), 2)
    # R$ adalah mata uang Real Brasil (sesuai dataset Olist)
    st.metric("Rata-rata Pengeluaran", value=f"R$ {avg_monetary}")

st.divider()

# ==========================================
# 4. VISUALISASI DISTRIBUSI
# ==========================================
st.subheader("Sebaran Pelanggan Berdasarkan Parameter RFM")

# Ukuran grafik disesuaikan agar pas di layar
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

# Grafik Recency (Waktu terakhir belanja)
sns.histplot(df['recency'], kde=True, ax=ax[0], color='#72BCD4')
ax[0].set_title("Recency (Hari Terakhir)", fontsize=14)
ax[0].set_xlabel("Hari")

# Grafik Frequency (Berapa kali belanja)
sns.histplot(df['frequency'], kde=True, ax=ax[1], color='#90BE6D')
ax[1].set_title("Frequency (Total Order)", fontsize=14)
ax[1].set_xlabel("Jumlah Transaksi")

# Grafik Monetary (Total uang belanja)
sns.histplot(df['monetary'], kde=True, ax=ax[2], color='#F9C74F')
ax[2].set_title("Monetary (Total Belanja)", fontsize=14)
ax[2].set_xlabel("Nilai Uang")

st.pyplot(fig)

# ==========================================
# 5. TABEL TOP CUSTOMERS
# ==========================================
st.subheader("5 Pelanggan dengan Pengeluaran Terbanyak")
top_5_customers = df.sort_values(by="monetary", ascending=False).head(5)

# Menampilkan tabel
st.table(top_5_customers[['customer_id', 'monetary']])

st.caption('Copyright © 2026 | Proyek Analisis Data - Dicoding Academy')