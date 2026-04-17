# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi tantangan serius berupa tingginya angka siswa yang tidak menyelesaikan pendidikan atau dropout. Masalah ini tidak hanya berdampak pada efisiensi institusi, tetapi juga pada keberhasilan akademik siswa secara keseluruhan. Untuk mengatasi hal tersebut, institusi berupaya melakukan deteksi dini terhadap siswa yang berisiko agar dapat memberikan bimbingan khusus dan intervensi yang tepat waktu guna menekan angka dropout.

### Permasalahan Bisnis
1. Jaya Jaya Institut menghadapi tantangan besar terkait tingginya angka dropout siswa, yang jika tidak segera ditangani, dapat mengancam reputasi unggul institusi yang telah dibangun sejak tahun 2000. Masalah bisnis utama yang perlu diselesaikan adalah ketidakmampuan institusi dalam mendeteksi secara dini siswa yang berisiko berhenti di tengah jalan, sehingga intervensi berupa bimbingan khusus sering kali terlambat Tingginya Angka Putus Kuliah (Dropout): Jaya Jaya Institut menghadapi masalah signifikan berupa banyaknya siswa yang tidak menyelesaikan pendidikan mereka meskipun institusi telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik.

2. Kebutuhan Deteksi Dini: Institusi membutuhkan mekanisme untuk mendeteksi siswa yang berisiko dropout sedini mungkin agar dapat memberikan intervensi berupa bimbingan khusus tepat waktu.

3. Penyajian Data yang Tidak Efektif: Terdapat kebutuhan untuk mengubah data mentah (seperti yang ada pada `data_student.csv`) menjadi visualisasi yang informatif dan efektif dengan menerapkan prinsip desain dan integritas data guna mendukung pengambilan keputusan.

4. Ketiadaan Alat Prediksi yang Siap Pakai: Belum tersedianya sistem atau prototype solusi machine learning yang mudah digunakan (user-friendly) oleh staf pengajar atau konselor akademik untuk melakukan prediksi status siswa secara mandiri.

5. Optimalisasi Penyaluran Bimbingan Khusus: Tanpa sistem deteksi yang akurat, pemberian bimbingan khusus menjadi tidak efisien. Masalah bisnis ini diselesaikan dengan memastikan bimbingan hanya difokuskan pada siswa dengan "Risiko Tinggi" berdasarkan analisis model.diberikan. Oleh karena itu, diperlukan sebuah solusi analitik berbasis machine learning yang mampu memprediksi status siswa secara akurat serta sebuah dashboard visualisasi data yang efektif untuk membantu pihak manajemen memahami faktor-faktor penyebab dropout demi pengambilan kebijakan yang lebih tepat sasaran.

### Cakupan Proyek
1. Analisis Data Eksploratif (EDA). Pada prosesnya melakukan pengolahan data awal untuk memahami karakteristik siswa. Cakupannya meliputi:
    - Identifikasi faktor-faktor utama yang berkontribusi terhadap keputusan siswa untuk berhenti sekolah (dropout), seperti faktor akademik (IPK/nilai semester), demografi, maupun status ekonomi.
    - Pembersihan data (data cleaning) dan penanganan data yang hilang atau tidak konsisten pada dataset data_student.csv.

2. Pengembangan model Machine Learning dengan membangun sistem cerdas untuk prediksi otomatis dengan tahapan:
    - Pemrosesan Data: Transformasi data kategori, skalarisasi data numerik (scaling), dan pembagian data menjadi training serta testing set.
    - Pelatihan Model: Menggunakan algoritma klasifikasi (seperti XGBoost yang terlihat pada notebook Anda) untuk memprediksi status siswa (Dropout, Graduate, atau Enrolled).
    - Evaluasi Model: Mengukur performa model menggunakan metrik seperti Accuracy, Precision, Recall, dan F1-Score untuk memastikan deteksi risiko dropout memiliki tingkat akurasi yang tinggi.

3. Pengembangan dashboard visualisasi dengan membuat media pelaporan yang interaktif dan informatif dengan prinsip desain yang baik, mencakup:
    - Visualisasi distribusi status siswa.
    - Grafik perbandingan antara performa akademik dengan status kelulusan.
    - Informasi demografis yang relevan untuk memberikan wawasan (insight) kepada manajemen institut.

4. Pembuatan Prototype Aplikasi (Streamlit) dengan mengembangkan aplikasi berbasis web sebagai solusi siap guna bagi user (staf/dosen), yang mencakup:
    - Antarmuka Prediksi Individual: Form input bagi user untuk memasukkan data siswa tertentu dan mendapatkan prediksi risiko secara real-time.
    - Sistem Peringatan Dini: Menampilkan status "Risiko Tinggi" atau "Risiko Rendah" beserta probabilitasnya.
    - Rekomendasi Tindakan: Memberikan saran otomatis (seperti bimbingan khusus) jika siswa terdeteksi berisiko dropout.

5. Dokumentasi dan panduan penggunaan dalam menyertakan langkah-langkah teknis untuk menjalankan solusi, mulai dari instalasi library yang dibutuhkan hingga cara menjalankan server lokal untuk prototype Streamlit tersebut.

### Persiapan
Sumber data: `data_student.csv` https://github.com/dicodingacademy/dicoding_dataset/blob/bce7a57a496d083716138922bc5839b5c30fa4ea/students_performance/data.csv 

Setup environment: Untuk menjalankan analisis data dan dashboard interaktif Jaya Jaya Institute, perlu mempersiapkan perangkat lunak, pustaka Python, dan struktur folder yang sesuai.


#### Install Perangkat Lunak Utama 
Memastikan perangkat lunak berikut sudah terinstal di komputer, berikut yang harus di install:
* **Python (Versi 3.13.13 atau lebih baru):** Bahasa pemrograman utama.
* **Visual Studio Code (VS Code):** Rekomendasi editor kode untuk menjalankan skrip Python dan Jupyter Notebook.
* **Web Browser:** Untuk menampilkan Dashboard Streamlit.

#### Install Perangkat lunak kedua
1. Setelah Pyhton dan Visual Studio Code (VS Code) terinstall di PC/Laptop, selanjutnya bisa membuka VS Code. Setelah VS Code terbuka cari icon Extensions biasanya di layar bagian kiri ketikan Python pada Search Extensions in Marketplace, selanjutnya install Extension Python setelah itu  klik tulisan "Terminal" di pojok kiri atas setelah itu muncul dashboard TERMINAL dan ketikan pada TERMINAL 
```bash
python --version  # untuk mengtahui python berhasil terinstall atau terhubung dengan VS Code
```
jika sudah muncul "Python 3.13.13" tandanya sudah terinstall. Tulisan "Python 3.14.2" yang muncul bisa jika versi yang digunakan berbeda. 

2. Buat *virtual environment* baru:
   ```bash
   python -m venv venv
   ```

3. Aktifkan *virtual environment*:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. Buat file `requirements.txt` dan isi dengan *library* berikut:
``` bash
pandas==2.3.3
streamlit==1.56.0
joblib==1.5.2
plotly==6.7.0
numpy==2.2.6
```

4. Selanjutnya Install All the Requirements Inside "requirements.txt" dengan mengetik perintah berikut di terminal:
``` bash
pip install -r requirements.txt 
``` 

5. Selanjutnya pastikan sudah memiliki file-file berikut dalam satu folder proyek:
    - notebook.ipynb
    - app.py
    - data_student.csv (wajib ada karena script app.py membacanya)
    - Folder models (isinya yaitu: `best_model_churn.pkl` dan `scaler.pkl`)
        submission/
        ├── model/
        │   ├── best_model_churn.pkl        # Model Random Forest hasil training (tersimpan)
        │   └── scaler.pkl                  # StandardScaler hasil training (tersimpan)
        ├── app.py                          # Aplikasi utama Streamlit
        ├── notebook.ipynb                  # Notebook eksplorasi data & pelatihan model
        ├── adetya_tino_dicoding-dashboard  # Screenshot dashboard
        ├── requirements.txt                # Daftar dependensi library
        └── README.md                       # Dokumentasi proyek ini
    - requirements.txt (jika belum ada, bisa membuatnya berdasarkan library yang digunakan di file yang telah di download atau bisa membuat manual).



## Business Dashboard
Dashboard ini dirancang sebagai alat bantu bagi staf Jaya Jaya Institut untuk memantau kondisi siswa dan melakukan intervensi dini. Fitur utamanya meliputi:
- Visualisasi Data Analitik (EDA): Menampilkan analisis data historis untuk memahami pola siswa yang melakukan dropout dibandingkan dengan yang lulus atau masih terdaftar.
- Prediksi Risiko Secara Real-time: Dashboard menyediakan antarmuka bagi pengguna untuk memasukkan data siswa (seperti status beasiswa, biaya kuliah, dan performa akademik semester 1 & 2) guna mendapatkan prediksi status siswa tersebut secara instan.
- Sistem Peringatan Dini: Jika sistem mendeteksi risiko tinggi, dashboard akan menampilkan peringatan berwarna merah bertuliskan "RISIKO TINGGI: SISWA BERPOTENSI DROPOUT" beserta probabilitas risikonya.
- Rekomendasi Tindakan: Dashboard tidak hanya memberikan prediksi, tetapi juga saran praktis seperti menghubungi konselor akademik jika siswa terdeteksi berisiko tinggi.


## Menjalankan Sistem Machine Learning
1. Persiapkan Lingkungan (Environment)
Buka terminal atau command prompt, lalu buat folder proyek dan pindahkan file app.py, data_student.csv, serta folder models yang berisi file model (`best_model_churn.pkl` dan `scaler.pkl`) ke dalam satu folder tersebut.

2. Menjalankan Aplikasi Streamlit
Gunakan perintah berikut di terminal untuk menjalankan server lokal aplikasi:

``` bash
streamlit run app.py
```
3. Mengakses Aplikasi Setelah perintah dijalankan, sistem akan otomatis membuka browser default dan menampilkan antarmuka dashboard pada alamat: http://localhost:8501 Fitur Utama Prototype. Setelah aplikasi berjalan, akan melihat beberapa bagian utama:
    - Overview Dashboard: Visualisasi ringkasan data siswa (EDA) menggunakan grafik interaktif dari Plotly.
    - Input Data Siswa: Di bilah samping (sidebar) atau panel utama, dapat memasukkan data seperti status beasiswa, IPK (grade), dan jumlah unit mata kuliah.
    - Hasil Prediksi: Sistem akan memberikan label "RISIKO TINGGI: SISWA BERPOTENSI DROPOUT" atau "RISIKO RENDAH" secara real-time.

4. Selain cara 1, 2, dan 3. Menjalankan Machine Learning secara langsung dapat mengakses 
**link Mengakses Prototype:** https://datascienceproject2-ls8yctqjaculgtx6fcd3fa.streamlit.app/ 


## Conclusion
Kesimpulan (Conclusion) dari proyek pengembangan sistem deteksi dropout siswa di Jaya Jaya Institut dapat dirangkum ke dalam beberapa poin strategis berikut:
1. Keberhasilan identifikasi adalah faktor kunci Melalui tahap Exploratory Data Analysis (EDA), proyek ini berhasil mengidentifikasi bahwa faktor akademik pada tahun pertama (Semester 1 dan Semester 2), status beasiswa, dan kondisi keuangan (seperti status tunggakan biaya kuliah) merupakan indikator terkuat yang membedakan antara siswa yang akan lulus (Graduate) dan siswa yang berisiko Dropout.
2. Performa model Machine Learning (XGBoost) yang dikembangkan menunjukkan performa yang sangat baik dalam mengklasifikasikan status siswa. Model ini mampu memberikan probabilitas risiko secara akurat, sehingga pihak institusi tidak lagi mengandalkan intuisi manual, melainkan pendekatan berbasis data (data-driven) untuk memprediksi masa depan akademik siswa.
3. Transformasi data menjadi solusi praktis, Proyek ini tidak hanya berhenti pada analisis statistik, tetapi berhasil mewujudkan solusi siap pakai berupa Dashboard Interaktif Streamlit. Solusi ini menjembatani kesenjangan teknis antara tim data dengan staf akademik, memungkinkan pengguna non-teknis untuk:
    -	Melihat visualisasi tren dropout secara langsung.
    -	Melakukan pengecekan mandiri terhadap data siswa tertentu melalui fitur prediksi.
4. Dampak strategis bagi Institusi, dengan adanya sistem peringatan dini (Early Warning System) ini, Jaya Jaya Institut kini memiliki kemampuan untuk:
    - Intervensi Tepat Sasaran: Bimbingan khusus dapat difokuskan hanya pada siswa yang memiliki probabilitas dropout tinggi, sehingga penggunaan sumber daya konselor lebih efisien.
    - Peningkatan Retensi: Deteksi dini diharapkan dapat menurunkan angka dropout secara signifikan dan menjaga reputasi institusi sebagai perguruan tinggi dengan tingkat kelulusan yang berkualitas.
5. Rekomendasi lanjutan, meskipun prototype sudah siap digunakan, disarankan agar model terus diperbarui (di-retrain) secara berkala dengan data terbaru untuk menjaga akurasi prediksi seiring dengan perubahan tren sosial-ekonomi atau kebijakan internal kampus di masa mendatang.


### Rekomendasi Action Items
Berdasarkan hasil analisis data dan sistem prediksi yang telah dibangun, berikut adalah rekomendasi action items strategis bagi Jaya Jaya Institut untuk menekan angka dropout dan mencapai target retensi siswa:
1. Implementasi Early Warning System (EWS) terintegrasi menjadikan prototype machine learning yang telah dibuat sebagai sistem operasional harian.
    - Aksi: Integrasikan model prediksi ke dalam sistem informasi akademik kampus.
    - Detail: Setiap akhir semester, data akademik siswa (IPK dan SKS) secara otomatis diproses oleh model. Siswa yang masuk kategori "Risiko Tinggi" akan langsung mendapatkan label peringatan di sistem yang hanya dapat dilihat oleh dosen pembimbing akademik.
2. Program intervensi finansial dan beasiswa tepat sasaran, Mengingat status pembayaran SPP (Tuition fees up to date) dan beasiswa adalah faktor krusial dalam data.
    -	Aksi: Memberikan skema bantuan keuangan atau cicilan khusus bagi siswa yang terdeteksi berisiko dropout karena kendala ekonomi.
    -	Detail: Alokasikan ulang sebagian dana beasiswa untuk program "Emergency Grant" bagi siswa berprestasi yang mendadak mengalami kendala finansial, agar mereka tidak terpaksa berhenti di tengah jalan.
3. Penguatan peran dosen Pembimbing Akademik (PA), Sistem tidak akan efektif tanpa sentuhan manusia.
    -	Aksi: Mewajibkan sesi konseling intensif bagi siswa yang terdeteksi berisiko oleh model.
    -	Detail: Dosen PA dibekali dengan data spesifik mengenai faktor apa yang membuat siswa tersebut berisiko (misalnya: nilai semester 2 yang anjlok). Fokus bimbingan diarahkan pada perbaikan akademik dan motivasi belajar sebelum masalah menumpuk.
4. Evaluasi kurikulum semester awal, data menunjukkan bahwa performa di Semester 1 dan 2 sangat menentukan keberlanjutan studi.
    -	Aksi: Melakukan audit terhadap mata kuliah di tahun pertama yang memiliki tingkat kegagalan tinggi.
    -	Detail: Jika ditemukan mata kuliah tertentu yang menjadi "penghambat" kelulusan, institut dapat menyediakan program tutorial tambahan atau kelas asistensi gratis bagi siswa yang kesulitan di mata kuliah tersebut.
5. Monitoring Pasca-Intervensi secara Berkala, memastikan bahwa bimbingan yang diberikan benar-benar berdampak.
    -	Aksi: Membuat feedback loop untuk memvalidasi akurasi model dan efektivitas bimbingan.
    -	Detail: Catat apakah siswa yang sebelumnya berstatus "Risiko Tinggi" berhasil lulus setelah diberi bimbingan. Data ini akan digunakan untuk melatih kembali (retrain) model agar semakin cerdas dari waktu ke waktu.


