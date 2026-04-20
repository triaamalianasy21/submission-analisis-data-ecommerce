# E-Commerce Data Analysis Dashboard 

## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Run streamlit app
streamlit run dashboard.py

## Project Structure
- `dashboard/`: Berisi file utama `dashboard.py` dan dataset yang telah dibersihkan `all_data.csv`.
- `data/`: Berisi dataset mentah.
- `notebook.ipynb`: Dokumentasi lengkap proses analisis data (Wrangling, EDA, Visualization).
- `requirements.txt`: library yang diperlukan untuk menjalankan aplikasi.
