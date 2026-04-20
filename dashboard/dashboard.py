import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# 1. Menyiapkan Data
# Pastikan file all_data.csv berada di folder yang sama dengan file dashboard.py ini
datetime_columns = ["order_purchase_timestamp"]
all_data = pd.read_csv("all_data.csv")
all_data.sort_values(by="order_purchase_timestamp", inplace=True)
all_data.reset_index(drop=True, inplace=True)

# Mengubah kolom menjadi datetime
for column in datetime_columns:
    all_data[column] = pd.to_datetime(all_data[column])

# --- SIDEBAR ---
with st.sidebar:
    # Logo (opsional)
    st.image("https://www.dicoding.com/blog/wp-content/uploads/2014/12/dicoding-header-logo.png")
    
    # Mengambil rentang waktu untuk batas kalender
    min_date = all_data["order_purchase_timestamp"].min().date()
    max_date = all_data["order_purchase_timestamp"].max().date()
    
    # Input Rentang Waktu (Interaktif)
    try:
        user_input = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
        
        # Logika proteksi agar tidak error saat user baru klik 1 tanggal
        if len(user_input) == 2:
            start_date, end_date = user_input
        else:
            start_date, end_date = user_input[0], user_input[0]
            
    except Exception:
        start_date, end_date = min_date, max_date

# Filter data utama berdasarkan input tanggal di sidebar
main_df = all_data[(all_data["order_purchase_timestamp"] >= str(start_date)) & 
                (all_data["order_purchase_timestamp"] <= str(end_date))]

# --- DASHBOARD MAIN PAGE ---
st.header('E-Commerce Dashboard 🛒')

# --- PERTANYAAN 1: KATEGORI TERLARIS ---
st.subheader('Top 10 Kategori Produk Terlaris')

if not main_df.empty:
    # Agregasi data kategori
    top_category = main_df.groupby('product_category_name_english')['order_id'].count().sort_values(ascending=False).head(10)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_category.values, y=top_category.index, color="#72BCD4", ax=ax)
    ax.set_xlabel("Jumlah Pesanan")
    ax.set_ylabel("Kategori")
    st.pyplot(fig)
else:
    st.warning("Tidak ada data pada rentang waktu ini.")

# --- PERTANYAAN 2: TREN PESANAN ---
st.subheader('Tren Pertumbuhan Pesanan')

if not main_df.empty:
    # Menyiapkan data tren bulanan
    # Kita pakai copy() agar tidak kena SettingWithCopyWarning
    trend_df = main_df.copy()
    trend_df['month_year'] = trend_df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    monthly_orders = trend_df.groupby('month_year')['order_id'].count().reset_index()

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(monthly_orders['month_year'], monthly_orders['order_id'], marker='o', linewidth=2, color="#72BCD4")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Pesanan")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("Pilih rentang waktu yang lebih luas untuk melihat tren.")

# Footer
st.caption(f'Copyright (c) Tria Amalia Anasya {pd.Timestamp.now().year}')