import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="📊 Dashboard Bank Data Kutai Barat",
    page_icon="📂",
    layout="wide"
)

# -------------------------
# Header dengan Logo
# -------------------------
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.image("logo_kutai_barat.png", width=100)   # ganti dengan file logo Pemkab Kutai Barat

with col2:
    st.markdown(
        """
        <h2 style='text-align: center; color: #2E86C1;'>
        📊 Dashboard Bank Data Kutai Barat
        </h2>
        <h4 style='text-align: center; color: gray;'>
        Bappeda Litbang Kutai Barat
        </h4>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("logo_bangga_melayani.png", width=100)   # ganti dengan file logo Bangga Melayani Bangsa



import streamlit as st
import pandas as pd

# -----------------------------
# KONFIGURASI APLIKASI
# -----------------------------
st.set_page_config(page_title="Aplikasi Satu Pintu Data", layout="wide")

st.title("📊Bank Data Bantuan")
st.markdown("Monitoring Program, Kegiatan, dan Penyaluran Bantuan secara **mudah & interaktif**.")

# -----------------------------
import streamlit as st

# Buat menu navigasi di sidebar
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    ["Input Data", "Lihat Data", "Analisis"]
)

# Gunakan menu
if menu == "Input Data":
    st.title("Halaman Input Data")
elif menu == "Lihat Data":
    st.title("Halaman Lihat Data")
elif menu == "Analisis":
    st.title("Halaman Analisis Data")


# Inisialisasi session state
if "data_bantuan" not in st.session_state:
    st.session_state.data_bantuan = pd.DataFrame(columns=[
        "Program", "Kegiatan", "Sub Kegiatan",
        "Nama Individu", "NIK Individu",
        "Nama Kelompok/UMKM", "Pengurus & Anggota", "NIK Kelompok",
        "Jenis Bantuan", "Rincian Bantuan", "Jumlah Bantuan", "Total Anggaran"
    ])

# -----------------------------
# MENU: INPUT DATA
# -----------------------------
if menu == "Input Data":
    st.header("✍️ Form Input Data Bantuan")

    col1, col2 = st.columns(2)

    with col1:
        program = st.text_input("Program")
        kegiatan = st.text_input("Kegiatan")
        sub_kegiatan = st.text_input("Sub Kegiatan")
        nama_individu = st.text_input("Nama (Individu)")
        nik_individu = st.text_input("NIK (Individu)")

    with col2:
        nama_kelompok = st.text_input("Nama Kelompok / UMKM")
        pengurus_anggota = st.text_area("Nama Pengurus & Anggota Kelompok")
        nik_kelompok = st.text_input("NIK (Kelompok)")
        jenis_bantuan = st.selectbox("Jenis Bantuan", ["Modal Usaha", "Alat Produksi", "Pelatihan", "Lainnya"])
        rincian_bantuan = st.text_area("Rincian Bantuan")

    jumlah_bantuan = st.number_input("Jumlah Bantuan (Rp)", min_value=0, step=1000)
    total_anggaran = st.number_input("Total Penyerapan Anggaran (Rp)", min_value=0, step=1000)

    if st.button("💾 Simpan Data"):
        new_data = pd.DataFrame([{
            "Program": program,
            "Kegiatan": kegiatan,
            "Sub Kegiatan": sub_kegiatan,
            "Nama Individu": nama_individu,
            "NIK Individu": nik_individu,
            "Nama Kelompok/UMKM": nama_kelompok,
            "Pengurus & Anggota": pengurus_anggota,
            "NIK Kelompok": nik_kelompok,
            "Jenis Bantuan": jenis_bantuan,
            "Rincian Bantuan": rincian_bantuan,
            "Jumlah Bantuan": jumlah_bantuan,
            "Total Anggaran": total_anggaran
        }])
        st.session_state.data_bantuan = pd.concat(
            [st.session_state.data_bantuan, new_data], ignore_index=True
        )
        st.success("✅ Data berhasil disimpan!")

# -----------------------------
# MENU: LIHAT DATA
# -----------------------------
elif menu == "Lihat Data":
    st.header("📑 Data Bantuan Tersimpan")
    st.dataframe(st.session_state.data_bantuan, use_container_width=True)

    # Tombol download
    if not st.session_state.data_bantuan.empty:
        csv = st.session_state.data_bantuan.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Data (CSV)", csv, "data_bantuan.csv", "text/csv")
    else:
        st.info("Belum ada data yang tersimpan.")

# -----------------------------
# MENU: STATISTIK
# -----------------------------
elif menu == "Statistik":
    st.header("📊 Statistik Data Bantuan")

    if not st.session_state.data_bantuan.empty:
        total_data = len(st.session_state.data_bantuan)
        total_jumlah = st.session_state.data_bantuan["Jumlah Bantuan"].sum()
        total_anggaran = st.session_state.data_bantuan["Total Anggaran"].sum()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Data", total_data)
        col2.metric("Total Jumlah Bantuan", f"Rp {total_jumlah:,.0f}")
        col3.metric("Total Anggaran", f"Rp {total_anggaran:,.0f}")

        # Grafik berdasarkan Jenis Bantuan
        st.subheader("📌 Grafik Jumlah Bantuan per Jenis Bantuan")
        chart_data = st.session_state.data_bantuan.groupby("Jenis Bantuan")["Jumlah Bantuan"].sum()
        st.bar_chart(chart_data)

    else:
        st.info("Belum ada data untuk ditampilkan.")

# -----------------------------
# MENU: TENTANG
# -----------------------------
elif menu == "Tentang":
    st.header("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat menggunakan **Streamlit** untuk mendukung pengelolaan data bantuan.  
    **Fitur utama**:
    - Input data bantuan lengkap 📋  
    - Tabel data dinamis 📑  
    - Statistik & grafik interaktif 📊  
    - Export data ke CSV ⬇️  
    """)
import streamlit as st
import pandas as pd

st.set_page_config(page_title="📂 Aplikasi Berbagi Data", layout="wide")
st.title("📂 Form Berbagi Data")

# Inisialisasi session state untuk menyimpan data upload
if "data_upload" not in st.session_state:
    st.session_state["data_upload"] = []

# ----------------------------
# FORM UPLOAD DATA
# ----------------------------
with st.form("form_berbagi_data"):
    st.subheader("📝 Upload Data Baru")

    nama_file = st.text_input("Nama File")
    format_file = st.selectbox("Format File", ["CSV", "Excel", "PDF", "Word", "Lainnya"])
    unit_kerja = st.text_input("Unit Kerja Pengupload")
    gambaran_umum = st.text_area("Gambaran Umum File")

    uploaded_file = st.file_uploader("Pilih File untuk Diupload", type=["csv", "xlsx", "pdf", "docx"])

    submitted = st.form_submit_button("📤 Upload Data")

    if submitted:
        if uploaded_file is not None:
            # Simpan ke session state
            st.session_state["data_upload"].append({
                "Nama File": nama_file,
                "Format": format_file,
                "Unit Kerja": unit_kerja,
                "Gambaran Umum": gambaran_umum,
                "Nama File Asli": uploaded_file.name
            })
            st.success(f"✅ File '{nama_file}' berhasil diupload oleh {unit_kerja}.")
        else:
            st.error("⚠️ Harap unggah file sebelum submit.")

# ----------------------------
# TABEL DATA UPLOAD
# ----------------------------
st.subheader("📑 Daftar Data yang Sudah Diupload")

if len(st.session_state["data_upload"]) > 0:
    df = pd.DataFrame(st.session_state["data_upload"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("Belum ada data yang diupload.")

import streamlit as st

st.set_page_config(
    page_title="📊 Dashboard Bank Data",
    page_icon="📂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Nama file background (letakkan di folder project)
sidebar_bg = "sidebar_bg.jpg"  

# CSS background + overlay
st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background: linear-gradient(
            rgba(0, 0, 0, 0.6),   /* overlay hitam transparan */
            rgba(0, 0, 0, 0.6)
        ), url("file:///{sidebar_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }}

    [data-testid="stSidebar"] * {{
        color: white !important;  /* teks putih agar kontras */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar Menu Navigasi
# -----------------------------
st.sidebar.title("🔎 Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:", 
    ["Beranda", "Input Data", "Statistik", "Tentang Aplikasi"]
)

# -----------------------------
# Konten sesuai pilihan
# -----------------------------
if menu == "Beranda":
    st.title("🏠 Beranda")
    st.info("Ini adalah halaman utama aplikasi.")

elif menu == "Input Data":
    st.title("✍️ Input Data")
    st.write("Form untuk menambahkan data.")

elif menu == "Statistik":
    st.title("📊 Statistik")
    st.write("Grafik & analisis data akan muncul di sini.")

elif menu == "Tentang Aplikasi":
    st.title("ℹ️ Tentang")
    st.write("Aplikasi Bank Data Kutai Barat - Bappeda Litbang.")
