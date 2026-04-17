import datetime
import pandas as pd
import streamlit as st
import joblib
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# KONFIGURASI HALAMAN 
st.set_page_config(
    page_title="Student Dropout Analytics | Jaya Jaya Institut",
    page_icon="🎓",
    layout="wide"
)

# LOAD MODEL & SCALER 
@st.cache_resource
def load_assets():
    # Pastikan path folder 'models' benar
    model = joblib.load('models/best_model_churn.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler

# LOAD DATA UNTUK EDA 
@st.cache_data
def load_data():
    # Menggunakan sep=';' karena data_student.csv menggunakan delimiter tersebut
    df = pd.read_csv('data_student.csv', sep=';')
    return df

# FUNGSI PREDIKSI 
def predict_student(data_input, model, scaler, feature_columns):
    # Pastikan urutan kolom di df_input persis sama dengan yang diharapkan scaler
    df_input = data_input[feature_columns]
    
    # Scaling
    scaled_data = scaler.transform(df_input)
    
    # Predict
    prediction = model.predict(scaled_data)
    
    # Probability
    prob = model.predict_proba(scaled_data)[:, 1]
    return prediction[0], prob[0]

# MAIN APP 
def main():
    # Load assets
    try:
        model, scaler = load_assets()
        df_raw = load_data()
        
        # PERBAIKAN: Gunakan urutan fitur dari scaler agar tidak error "Feature names match"
        if hasattr(scaler, 'feature_names_in_'):
            feature_cols = scaler.feature_names_in_.tolist()
        else:
            # Fallback jika scaler tidak menyimpan nama fitur
            feature_cols = df_raw.drop(columns=['Status']).columns.tolist()
            
    except Exception as e:
        st.error(f"Gagal memuat model atau data: {e}")
        return

    # Sidebar
    st.sidebar.image("https://www.dicoding.com/blog/wp-content/uploads/2014/12/dicoding-header-logo.png", width=200)
    st.sidebar.title("Navigasi")
    menu = st.sidebar.radio("Pilih Menu:", ["Business Overview", "Data Dashboard", "Dropout Predictor"])

    # 1. BUSINESS OVERVIEW
    if menu == "Business Overview":
        st.title("Sistem Deteksi Dini Dropout Mahasiswa")
        st.subheader("Jaya Jaya Institut")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            ### Latar Belakang
            Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi tantangan serius berupa tingginya angka siswa yang tidak menyelesaikan pendidikan atau dropout. 
            Masalah ini tidak hanya berdampak pada efisiensi institusi, tetapi juga pada keberhasilan akademik siswa secara keseluruhan. Untuk mengatasi hal tersebut, institusi berupaya melakukan deteksi dini terhadap siswa yang berisiko agar dapat memberikan bimbingan khusus dan intervensi yang tepat waktu guna menekan angka dropout.

            ### Tujuan Proyek
            1. Analisis Data Eksploratif (EDA). Tahap ini bertujuan untuk mengenal dan membersihkan data dimana 
            Fokus utamanya adalah mengidentifikasi variabel kunci (seperti nilai akademik dan ekonomi) yang memicu dropout serta memastikan dataset data_student.csv siap digunakan tanpa ada data yang rusak atau hilang.

            2. Pengembangan model Machine Learning adalah proses pembangunan otak sistem. 
            Meliputi persiapan data teknis (seperti scaling), pelatihan algoritma klasifikasi (seperti XGBoost), dan pengujian akurasi menggunakan metrik evaluasi untuk memastikan prediksi status siswa benar-benar presisi.

            3. Pengembangan dashboard visualisasi untuk pembuatan media pelaporan interaktif. 
            Fokusnya adalah menyajikan temuan data dalam bentuk grafik yang mudah dipahami, seperti distribusi status siswa dan tren akademik, guna membantu manajemen mengambil keputusan berbasis data secara cepat.

            4. Pembuatan prototype aplikasi (Streamlit) adalah Pengembangan solusi praktis berbasis web. 
            Aplikasi ini memungkinkan staf atau dosen untuk memasukkan data siswa secara mandiri, mendapatkan prediksi risiko secara real-time, serta menerima saran tindakan (seperti bimbingan) secara otomatis.

            5. Dokumentasi dan panduan penggunaan untuk Penyusunan instruksi teknis. 
            Bagian ini menjamin keberlanjutan proyek dengan menyediakan panduan lengkap mengenai instalasi library, konfigurasi sistem, hingga cara menjalankan server lokal untuk mengoperasikan aplikasi.
            """)
        
        with col2:
            st.info(f"**Total Database Mahasiswa:** {len(df_raw)} orang")
            dropout_rate = (df_raw['Status'] == 'Dropout').mean() * 100
            st.metric("Tingkat Dropout Saat Ini", f"{dropout_rate:.2f}%")
            
            total_mhs = len(df_raw)
            total_dropout = len(df_raw[df_raw['Status'] == 'Dropout'])
            total_graduate = len(df_raw[df_raw['Status'] == 'Graduate'])
        
            m1, m2 = st.columns(2)
            m1.metric("Total Dropout", f"{total_dropout}", delta=f"{(total_dropout/total_mhs*100):.1f}%", delta_color="inverse")
            m2.metric("Total Graduate", f"{total_graduate}", delta=f"{(total_graduate/total_mhs*100):.1f}%")

# 2. DATA DASHBOARD (EDA)

    elif menu == "Data Dashboard":
        st.title("Analisis Data Mahasiswa")

        col_a, col_b = st.columns(2)

        with col_a:
            st.subheader("Distribusi Status Mahasiswa")
            fig_status = px.pie(df_raw, names='Status', color='Status',
                               color_discrete_map={'Graduate':'#2ecc71', 'Dropout':'#e74c3c', 'Enrolled':'#f1c40f'},
                               hole=0.4)
            st.plotly_chart(fig_status, use_container_width=True)
            st.success("Mayoritas mahasiswa berhasil menyelesaikan studinya (Graduate), diikuti oleh mahasiswa yang berhenti di tengah jalan (Dropout), dan sebagian kecil masih dalam masa perkuliahan (Enrolled). " \
            "Dari visual, terlihat angka Dropout cukup signifikan (mendekati sepertiga dari total data). Meskipun tingkat kelulusan cukup tinggi, angka Dropout yang mencapai kisaran 30-32% menunjukkan perlunya intervensi khusus untuk menahan laju mahasiswa yang keluar sebelum lulus.")

        with col_b:
            st.subheader("Status Berdasarkan Beasiswa")
            df_viz = df_raw.copy()
            df_viz['Scholarship'] = df_viz['Scholarship_holder'].map({1: 'Penerima', 0: 'Bukan Penerima'})
            fig_scholar = px.histogram(df_viz, x='Scholarship', color='Status', barmode='group',
                                      color_discrete_map={'Graduate':'#2ecc71', 'Dropout':'#e74c3c', 'Enrolled':'#f1c40f'})
            st.plotly_chart(fig_scholar, use_container_width=True)
            st.success("Proporsi kelulusan (Graduate) jauh lebih besar pada kelompok penerima beasiswa dibandingkan dengan non-penerima. Sebaliknya, persentase Dropout jauh lebih tinggi pada mahasiswa yang tidak mendapatkan beasiswa. Dukungan finansial berperan penting dalam retensi mahasiswa. " \
            "Beasiswa terbukti menjadi faktor motivasi atau bantuan krusial yang membantu mahasiswa bertahan hingga lulus. Mahasiswa non-beasiswa memiliki risiko kerentanan ekonomi yang lebih tinggi untuk putus sekolah.") 

        st.divider()
        st.subheader("Pengaruh Nilai Semester terhadap Risiko Dropout")
        col_c, col_d = st.columns(2)
    
        with col_c:
            fig_grade1 = px.box(df_raw, x='Status', y='Curricular_units_1st_sem_grade', color='Status',
                                labels={"Curricular_units_1st_sem_grade": "Nilai Semester 1"},
                               title="Nilai Semester 1",
                               color_discrete_map={'Graduate':'#2ecc71', 'Dropout':'#e74c3c', 'Enrolled':'#f1c40f'})
            st.plotly_chart(fig_grade1, use_container_width=True)
            st.success("Terdapat korelasi positif yang sangat kuat (linier). Mahasiswa yang berada di area kanan atas (nilai tinggi di kedua semester) didominasi oleh warna hijau (Graduate). " \
            "Sebaliknya, terdapat penumpukan titik-titik merah (Dropout) di titik $(0,0)$, yang mengindikasikan banyak mahasiswa dropout bahkan tidak menyelesaikan atau tidak memiliki nilai di kedua semester tersebut. Performa akademik awal adalah prediktor terbaik. " \
            "Jika seorang mahasiswa mulai menunjukkan penurunan nilai atau mendapatkan nilai nol di semester pertama, kemungkinan besar mereka akan berstatus Dropout di semester kedua.")  

        with col_d:
            fig_grade2 = px.box(df_raw, x='Status', y='Curricular_units_2nd_sem_grade', color='Status',
                                labels={"Curricular_units_2nd_sem_grade": "Nilai Semester 2"},
                               title="Nilai Semester 2",
                               color_discrete_map={'Graduate':'#2ecc71', 'Dropout':'#e74c3c', 'Enrolled':'#f1c40f'})
            st.plotly_chart(fig_grade2, use_container_width=True)
            st.success("Terdapat korelasi positif yang sangat kuat (linier). Mahasiswa yang berada di area kanan atas (nilai tinggi di kedua semester) didominasi oleh warna hijau (Graduate). " \
            "Sebaliknya, terdapat penumpukan titik-titik merah (Dropout) di titik $(0,0)$, yang mengindikasikan banyak mahasiswa dropout bahkan tidak menyelesaikan atau tidak memiliki nilai di kedua semester tersebut. Performa akademik awal adalah prediktor terbaik. " \
            "Jika seorang mahasiswa mulai menunjukkan penurunan nilai atau mendapatkan nilai nol di semester pertama, kemungkinan besar mereka akan berstatus Dropout di semester kedua.")

# 3. DROPOUT PREDICTOR
    elif menu == "Dropout Predictor":
        st.title("Prediksi Risiko Dropout")
        st.write("Masukkan data mahasiswa di bawah ini untuk melihat hasil prediksi.")

        with st.form("input_form"):
            st.markdown("### Jalur & Program Studi")
            col_new1, col_new2 = st.columns(2)
            with col_new1:
                jalur_map = {"Fase 1 - Umum": 1, "Fase 2 - Umum": 2, "Usia > 23 Tahun": 5,
                    "Pindah Jurusan": 7, "Diploma Spesialisasi": 10, "Lulusan PT Lain": 15,
                    "Fase 3 - Umum": 17, "Transfer": 18, "Pindah Kampus/Jurusan": 19
                }
                jalur_pilihan = st.selectbox("Jalur Pendaftaran", list(jalur_map.keys()))
            with col_new2:
                prodi_map = {"Keperawatan": 9500, "Manajemen": 9147, "Layanan Sosial": 9238,
                    "Keperawatan Hewan": 9003, "Jurnalisme & Komunikasi": 9085,
                    "Pariwisata": 9254, "Desain Komunikasi": 9119, "Agronomi": 9070}
                prodi_pilihan = st.selectbox("Program Studi", list(prodi_map.keys()))

            st.divider()
            st.markdown("### Informasi Dasar & Akademik")
            c1, c2, c3 = st.columns(3)
            with c1:
                gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
                age = st.number_input("Usia saat Pendaftaran", 17, 70, 20)
            with c2:
                marital = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
                tuition = st.selectbox("Biaya Kuliah Lunas?", ["Tidak", "Ya"])
            with c3:
                scholarship = st.selectbox("Penerima Beasiswa?", ["Tidak", "Ya"])
                debtor = st.selectbox("Punya Hutang?", ["Tidak", "Ya"])

            st.markdown("### Performa Akademik (Skala 4.00)")
            c4, c5, c6 = st.columns(3)
            with c4:
                u1_enrolled = st.number_input("Unit Sem 1 Terdaftar", 0, 30, 6)
                u1_approved = st.number_input("Unit Sem 1 Lulus", 0, 30, 6)
                # Input menggunakan skala 4.00
                u1_grade_4 = st.number_input("IPK Semester 1", 0.0, 4.0, 3.0, step=0.01)
            with c5:
                u2_enrolled = st.number_input("Unit Sem 2 Terdaftar", 0, 30, 6)
                u2_approved = st.number_input("Unit Sem 2 Lulus", 0, 30, 6)
                # Input menggunakan skala 4.00
                u2_grade_4 = st.number_input("IPK Semester 2", 0.0, 4.0, 3.0, step=0.01)
            with c6:
                # Nilai Masuk dan Kualifikasi biasanya skala 0-200, jika ingin 4.0 juga:
                admission_grade_4 = st.number_input("Nilai Masuk (Skala 4.00)", 0.0, 4.0, 2.5, step=0.01)
                unemployment = st.number_input("Laju Pengangguran (%)", 0.0, 20.0, 7.0)
            
            submit = st.form_submit_button(" Jalankan Prediksi")

        if submit:
            mapping_gender = {"Perempuan": 0, "Laki-laki": 1}
            mapping_bool = {"Tidak": 0, "Ya": 1}
            mapping_marital = {"Single": 1, "Married": 2, "Divorced": 4}

            # Konversi balik dari skala 4.0 ke skala 20 (untuk Grade) dan skala 200 (untuk Admission)
            u1_grade_final = u1_grade_4 * 5.0
            u2_grade_final = u2_grade_4 * 5.0
            admission_final = admission_grade_4 * 50.0 # Karena skala asli Admission adalah 0-200

            # Mengisi semua kolom yang diminta model (36-38 kolom sesuai scaler) dengan median
            input_dict = {col: float(df_raw[col].median()) for col in feature_cols if col in df_raw.columns}
            
            # Timpa dengan input dari user (sudah dikonversi ke skala asli model)
            input_dict.update({
                'Application_mode': jalur_map[jalur_pilihan], 
                'Course': prodi_map[prodi_pilihan],           
                'Gender': mapping_gender[gender],
                'Age_at_enrollment': age,
                'Scholarship_holder': mapping_bool[scholarship],
                'Marital_status': mapping_marital[marital],
                'Tuition_fees_up_to_date': mapping_bool[tuition],
                'Debtor': mapping_bool[debtor],
                'Curricular_units_1st_sem_enrolled': u1_enrolled,
                'Curricular_units_1st_sem_approved': u1_approved,
                'Curricular_units_1st_sem_grade': u1_grade_final,      
                'Curricular_units_2nd_sem_enrolled': u2_enrolled,
                'Curricular_units_2nd_sem_approved': u2_approved,
                'Curricular_units_2nd_sem_grade': u2_grade_final,      
                'Admission_grade': admission_final,
                'Unemployment_rate': unemployment
            })

            input_df = pd.DataFrame([input_dict])
            
            # Pastikan kolom lengkap sebelum masuk ke predict_student
            for col in feature_cols:
                if col not in input_df.columns:
                    input_df[col] = 0.0 

            res, prob = predict_student(input_df, model, scaler, feature_cols)

            st.divider()
            st.subheader("Hasil Analisis")
            if res == 1:
                st.error(f"### RISIKO TINGGI: MAHASISWA BERPOTENSI DROPOUT")
                st.write(f"Probabilitas Risiko: **{prob*100:.1f}%**")
            else:
                st.success(f"### RISIKO RENDAH: MAHASISWA CENDERUNG BERTAHAN")
                st.write(f"Probabilitas Aman: **{(1-prob)*100:.1f}%**")

    # Footer
    st.sidebar.divider()
    year = datetime.date.today().year
    st.sidebar.caption(f"Copyright © {year} | Adetya Tino Forrestiawan")

if __name__ == '__main__':
    main()