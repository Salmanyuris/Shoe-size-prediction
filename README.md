# Prediksi Ukuran Sepatu Berdasarkan Tinggi Badan
### Tugas Kelompok 2 – PBL Machine Learning

Proyek ini merupakan implementasi **Machine Learning menggunakan metode Linear Regression** untuk memprediksi ukuran sepatu seseorang berdasarkan tinggi badannya.

Model dilatih menggunakan dataset yang berisi pasangan data tinggi badan dan ukuran sepatu. Selanjutnya, model mempelajari hubungan antara kedua variabel tersebut untuk menghasilkan prediksi ukuran sepatu berdasarkan tinggi badan yang diberikan.

## 🎯 Tujuan Proyek

1. Memahami penerapan algoritma Linear Regression.
2. Menganalisis hubungan antara tinggi badan dan ukuran sepatu.
3. Melakukan proses Exploratory Data Analysis (EDA).
4. Melatih model menggunakan data training.
5. Mengevaluasi performa model menggunakan data testing.
6. Melakukan prediksi ukuran sepatu berdasarkan data baru.

## 🛠️ Teknologi dan Library

Proyek ini menggunakan beberapa teknologi dan library Python berikut:

| Teknologi / Library | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Google Colab | Lingkungan pengembangan dan eksekusi program |
| NumPy | Pengolahan data numerik |
| Pandas | Membaca dan mengelola dataset |
| Matplotlib | Visualisasi data |
| Scikit-learn | Implementasi Linear Regression dan evaluasi model |
| SciPy | Mendukung pengolahan statistik |

## 📊 Dataset

Dataset yang digunakan berisi dua variabel utama:

| Variabel | Keterangan |
|---|---|
| X (Independent Variable) | Tinggi Badan |
| Y (Dependent Variable) | Ukuran Sepatu |

Dataset disimpan dalam format CSV dan diakses melalui Google Drive.

**Dataset:** [Google Drive – Dataset Prediksi Ukuran Sepatu](https://drive.google.com/uc?id=12y4yjLottmCkwRcky7uH_3lneQluY5tC)

## ⚙️ Tahapan Proses Machine Learning

### 1. Import Library
Mengimpor library yang dibutuhkan untuk pengolahan data, visualisasi, pembuatan model, dan evaluasi.

### 2. Menghubungkan Google Drive
Menghubungkan Google Colab dengan Google Drive untuk mengakses dataset.

### 3. Import Dataset
Membaca dataset CSV menggunakan Pandas.

### 4. Exploratory Data Analysis (EDA)
Melakukan analisis awal terhadap dataset melalui beberapa visualisasi:

- **KDE Plot:** Melihat distribusi data tinggi badan dan ukuran sepatu.
- **Boxplot:** Mengidentifikasi persebaran data dan kemungkinan outlier.
- **Scatter Plot:** Melihat hubungan antara tinggi badan dan ukuran sepatu.
- **Correlation:** Menghitung korelasi antara kedua variabel.

### 5. Menentukan Variabel X dan Y
Menentukan variabel independen dan dependen:

- X = Tinggi Badan.
- Y = Ukuran Sepatu.

### 6. Membagi Data Training dan Testing
Dataset dibagi menggunakan `train_test_split()` dengan komposisi:

- 65% untuk data training.
- 35% untuk data testing.

### 7. Membuat dan Melatih Model
Membuat model menggunakan algoritma `LinearRegression()` dari Scikit-learn, kemudian melatihnya menggunakan data training melalui fungsi `fit()`.

### 8. Menentukan Koefisien dan Intercept
Mengambil nilai koefisien regresi (M) dan intercept (b) untuk membentuk persamaan regresi linear.

Rumus Linear Regression:

**Y = M(X) + b**

Keterangan:
- Y = Hasil prediksi ukuran sepatu.
- M = Koefisien regresi (slope).
- X = Tinggi badan.
- b = Intercept (konstanta).

### 9. Evaluasi Model
Mengukur performa model menggunakan data testing dengan beberapa metrik evaluasi:

| Metrik | Keterangan |
|---|---|
| MAE (Mean Absolute Error) | Mengukur rata-rata selisih absolut antara nilai aktual dan prediksi. |
| MSE (Mean Squared Error) | Mengukur rata-rata kuadrat selisih antara nilai aktual dan prediksi. |
| Median Absolute Error | Mengukur nilai tengah dari selisih absolut antara nilai aktual dan prediksi. |
| R² Score | Mengukur kemampuan model dalam menjelaskan variasi data aktual. |

### 10. Prediksi Data Baru
Model digunakan untuk memprediksi ukuran sepatu berdasarkan tinggi badan baru.

Contoh input:

```python
tinggi_badan = 164.5
```

Model akan menghasilkan prediksi ukuran sepatu berdasarkan tinggi badan tersebut.

### 11. Perbandingan Data Aktual dan Prediksi
Membuat tabel perbandingan yang berisi:

- Tinggi Badan.
- Data Aktual.
- Data Prediksi.

Hasil perbandingan digunakan untuk melihat perbedaan antara ukuran sepatu aktual dan hasil prediksi model.

## 🚀 Cara Menjalankan Program

1. Buka [Google Colab](https://colab.research.google.com/).
2. Buat notebook baru.
3. Salin kode program ke dalam notebook.
4. Pastikan dataset Google Drive dapat diakses.
5. Jalankan seluruh kode program secara berurutan.
6. Amati hasil visualisasi, evaluasi model, dan prediksi ukuran sepatu.

## 📁 Struktur Repository

```text
Prediksi-Ukuran-Sepatu/
│
├── README.md
│
└── Prediksi_Ukuran_Sepatu.ipynb
```

## 📌 Kesimpulan

Melalui proyek ini, algoritma Linear Regression diterapkan untuk memprediksi ukuran sepatu berdasarkan tinggi badan. Proses dimulai dari pengumpulan dan analisis dataset, pembagian data training dan testing, pelatihan model, hingga evaluasi dan prediksi menggunakan data baru.

Hasil evaluasi model dapat digunakan untuk mengetahui seberapa baik algoritma Linear Regression dalam mempelajari hubungan antara tinggi badan dan ukuran sepatu.

---

**Tugas Kelompok 2 – PBL Machine Learning**  
**Metode:** Linear Regression  
**Topik:** Prediksi Ukuran Sepatu Berdasarkan Tinggi Badan
