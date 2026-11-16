
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard",
                   page_icon="🚲",
                   layout="wide")

# Memuat dataset
@st.cache_data
def load_data():
    df = pd.read_csv("hour.csv")
    df["dteday"] = pd.to_datetime(df["dteday"])

    season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}

    weather_map = {1: "Clear", 2: "Mist/Cloudy",
                   3: "Light Rain/Snow", 4: "Heavy Rain/Snow"}

    df["season_label"] = df["season"].map(season_map)
    df["weather_label"] = df["weathersit"].map(weather_map)

    df["day_type"] = df["workingday"].map({0: "Hari Bukan Kerja", 1: "Hari Kerja"})

    return df

df = load_data()

# Judul dashboard
st.title("🚲 Bike Sharing Dashboard")
st.write("Dashboard Analisis Pola Penyewaan Sepeda "
         "Berdasarkan Waktu, Musim, Cuaca, dan Karakteristik Pengguna")
st.divider()

# Filter pada sidebar
st.sidebar.header("Filter Data")

start_date = st.sidebar.date_input("Tanggal Awal",
                                   value=df["dteday"].min().date(),
                                   min_value=df["dteday"].min().date(),
                                   max_value=df["dteday"].max().date())

end_date = st.sidebar.date_input("Tanggal Akhir", 
                                 value=df["dteday"].max().date(),
                                 min_value=df["dteday"].min().date(),
                                 max_value=df["dteday"].max().date())

seasons = st.sidebar.multiselect("Pilih Musim",
                                 options=df["season_label"].unique(),
                                 default=df["season_label"].unique())

weather = st.sidebar.multiselect("Pilih Kondisi Cuaca",
                                 options=df["weather_label"].unique(),
                                 default=df["weather_label"].unique())

# Memfilter data
if start_date > end_date:
    st.error("Tanggal awal tidak boleh melebihi tanggal akhir.")
    st.stop()

filtered_df = df[(df["dteday"].dt.date >= start_date) &
                 (df["dteday"].dt.date <= end_date) &
                 (df["season_label"].isin(seasons)) &
                 (df["weather_label"].isin(weather))]

if filtered_df.empty:
    st.warning("Tidak ada data untuk kombinasi filter tersebut.")
    st.stop()

# KPI
st.subheader("Ringkasan Penyewaan")

total_rentals = filtered_df["cnt"].sum()
total_casual = filtered_df["casual"].sum()
total_registered = filtered_df["registered"].sum()
average_rentals = filtered_df["cnt"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Penyewaan", f"{total_rentals:,.0f}")
col2.metric("Pengguna Casual", f"{total_casual:,.0f}")
col3.metric("Pengguna Registered", f"{total_registered:,.0f}")
col4.metric("Rata-rata per Jam", f"{average_rentals:,.2f}")

st.divider()

# Grafik 1: Pola penyewaan berdasarkan jam
st.subheader("1. Pola Penyewaan Berdasarkan Jam")

hourly_rentals = (filtered_df.groupby(["hr", "day_type"], observed=True)["cnt"].mean().unstack())

fig, ax = plt.subplots(figsize=(12, 5))

for column in hourly_rentals.columns:
    ax.plot(hourly_rentals.index,
            hourly_rentals[column],
            marker="o",
            linewidth=2,
            label=column)

ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
ax.set_xticks(range(24))
ax.set_xlim(0, 23)
ax.set_xticklabels([f"{hour:02d}.00" for hour in range(24)])
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.legend(title="Jenis Hari")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.caption("Grafik menunjukkan perbandingan rata-rata penyewaan "
           "sepeda setiap jam antara hari kerja dan hari bukan kerja")


# Grafik 2 dan 3: Penyewaan berdasarkan cuaca dan musim
col1, col2 = st.columns(2)

with col1:
    st.subheader("2. Penyewaan Berdasarkan Cuaca")

    weather_order = ["Clear", "Mist/Cloudy", "Light Rain/Snow", "Heavy Rain/Snow"]

    weather_rentals = (filtered_df.groupby("weather_label")["cnt"].mean()
                       .reindex(weather_order).dropna())

    fig, ax = plt.subplots(figsize=(8, 5))

    colors = ["#491204", "#9F1919", "#A54949", "#AC7B7B"]

    bars = ax.bar(weather_rentals.index,
                  weather_rentals.values,
                  color=colors[:len(weather_rentals)],
                  width=0.65)

    ax.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Jumlah Penyewaan")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    ax.bar_label(bars, fmt="%.1f", padding=3)
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.subheader("3. Penyewaan Berdasarkan Musim")

    season_order = ["Spring", "Summer", "Fall", "Winter"]

    season_rentals = (filtered_df.groupby("season_label")["cnt"].mean()
                      .reindex(season_order).dropna())

    fig, ax = plt.subplots(figsize=(8, 5))

    colors = ["#8C8DBE", "#5750A7", "#3026C2", "#0E054B"]

    bars = ax.bar(season_rentals.index,
                  season_rentals.values,
                  color=colors[:len(season_rentals)],
                  width=0.65)

    ax.set_title("Rata-rata Penyewaan Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Jumlah Penyewaan")
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    ax.bar_label(bars, fmt="%.1f", padding=3)
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


# Grafik 4: Perbandingan Jenis Pengguna
st.subheader("4. Perbandingan Jenis Pengguna")

user_rentals = (filtered_df.groupby("day_type", observed=True)[["casual", "registered"]].mean()
                .reindex(["Hari Bukan Kerja", "Hari Kerja"]))

fig, ax = plt.subplots(figsize=(10, 5))

x = np.arange(len(user_rentals.index))
width = 0.35

bars1 = ax.bar(x - width / 2,
               user_rentals["casual"],
               width, label="Casual",
               color="#579C75")

bars2 = ax.bar(x + width / 2,
               user_rentals["registered"],
               width, label="Registered",
               color="#0B481E")

ax.set_title("Rata-rata Penyewaan Berdasarkan Jenis Pengguna")
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda")
ax.set_xticks(x)
ax.set_xticklabels(user_rentals.index)
ax.legend(title="Jenis Pengguna")
ax.grid(axis="y", linestyle="--", alpha=0.3)
ax.set_axisbelow(True)

ax.bar_label(bars1, fmt="%.1f", padding=3)
ax.bar_label(bars2, fmt="%.1f", padding=3)

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.caption("Grafik membandingkan rata-rata penyewaan pengguna casual "
           "dan registered berdasarkan jenis hari")

# Tabel data
with st.expander("Lihat Data Penyewaan"):
    st.dataframe(filtered_df, use_container_width=True)

st.caption("Sumber data: Bike Sharing Dataset, periode 2011–2012.")
