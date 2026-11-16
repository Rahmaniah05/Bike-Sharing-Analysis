# Analisis Data Bike Sharing

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda (*Bike Sharing*) selama periode 2011–2012. Analisis dilakukan untuk mengetahui hubungan pola penyewaan dengan waktu, kondisi cuaca, musim, serta karakteristik pengguna.

Proyek ini menggunakan Python dengan beberapa library, seperti Pandas, NumPy, Matplotlib, dan Seaborn untuk proses pengolahan, eksplorasi, dan visualisasi data. Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Business Questions

Analisis ini berfokus pada tiga pertanyaan bisnis berikut:

1. Bagaimana pola rata-rata jumlah penyewaan sepeda berdasarkan jam dalam satu hari, serta bagaimana perbedaannya antara hari kerja dan hari libur selama periode 2011–2012?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca dan musim selama periode 2011–2012?
3. Bagaimana perbandingan jumlah penyewaan sepeda oleh pengguna casual dan registered antara hari kerja dan hari libur selama periode 2011–2012?

## Dataset

Dataset yang digunakan terdiri dari dua file:

- `hour.csv`: Data penyewaan sepeda berdasarkan jam.
- `day.csv`: Data penyewaan sepeda berdasarkan hari.

Dataset mencakup periode 1 Januari 2011 hingga 31 Desember 2012.

## Tahapan Analisis

1. Menentukan pertanyaan bisnis.
2. Mengimpor library yang dibutuhkan.
3. Melakukan *data wrangling*, meliputi pengumpulan, penilaian, dan pembersihan data.
4. Melakukan *Exploratory Data Analysis* (EDA).
5. Melakukan visualisasi dan analisis data.
6. Melakukan analisis lanjutan menggunakan pengelompokan waktu (*time binning*).
7. Menyusun kesimpulan dan rekomendasi.

## Hasil Analisis

Beberapa hasil utama dari analisis yang dilakukan adalah:

- Total penyewaan sepeda selama periode pengamatan mencapai 3.292.679 kali.
- Pengguna registered mendominasi penyewaan sebesar 81,17%, sedangkan pengguna casual sebesar 18,83%.
- Pada hari kerja, rata-rata penyewaan tertinggi terjadi pada pukul 17.00, sedangkan pada hari bukan kerja terjadi pada pukul 13.00.
- Rata-rata penyewaan tertinggi berdasarkan kondisi cuaca terjadi pada cuaca cerah atau sedikit berawan.
- Berdasarkan musim, rata-rata penyewaan tertinggi terjadi pada musim gugur (*Fall*).
- Berdasarkan pengelompokan waktu, periode sore memiliki rata-rata penyewaan tertinggi sebesar 362,54 sepeda per jam.

## Dashboard

Dashboard interaktif dibuat menggunakan Streamlit untuk menampilkan ringkasan penyewaan, pola penyewaan berdasarkan jam, kondisi cuaca, musim, dan jenis pengguna.

**Link Dashboard:**

https://bike-sharing-analysis-dsrahmaniah.streamlit.app/

## Tools dan Library

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Google Colab
- Visual Studio Code
- GitHub

## Cara Menjalankan Dashboard

1. Clone repository:

   ```bash
   git clone https://github.com/Rahmaniah05/Bike-Sharing-Analysis.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd Bike-Sharing-Analysis
   ```

3. Buat virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Aktifkan virtual environment:

   ```bash
   .venv\Scripts\activate
   ```

5. Instal library yang dibutuhkan:

   ```bash
   pip install -r requirements.txt
   ```

6. Jalankan dashboard:

   ```bash
   streamlit run dashboard.py
   ```

---

**Proyek Analisis Data – Bike Sharing | 2011–2012**