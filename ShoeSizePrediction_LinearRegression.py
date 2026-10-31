# ============================================================
# TUGAS KELOMPOK 2 - PBL MACHINE LEARNING
# Prediksi Ukuran Sepatu Berdasarkan Tinggi Badan
# Menggunakan Metode Linear Regression
# ============================================================


# ============================================================
# 1. IMPORT LIBRARY
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm

from scipy import stats


# ============================================================
# 2. MENENTUKAN LOKASI DATASET
# ============================================================

# URL dataset yang tersimpan di Google Drive
input_file = 'https://drive.google.com/uc?id=12y4yjLottmCkwRcky7uH_3lneQluY5tC'


# ============================================================
# 3. MENGHUBUNGKAN GOOGLE COLAB DENGAN GOOGLE DRIVE
# ============================================================

from google.colab import drive

drive.mount('/content/drive')


# ============================================================
# 4. IMPORT DATASET
# ============================================================

# Membaca dataset dalam format CSV
data = pd.read_csv(input_file, sep=',', header=None)


# ============================================================
# 5. EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

# ------------------------------------------------------------
# 5.1 Distribusi Data Tinggi Badan (X)
# ------------------------------------------------------------

eda = plt.figure(figsize=(12, 4))

eda.add_subplot(1, 2, 1)
data[0].plot(kind='kde')

eda.add_subplot(1, 2, 1)
plt.boxplot(data[0])

plt.show()


# ------------------------------------------------------------
# 5.2 Distribusi Data Ukuran Sepatu (Y)
# ------------------------------------------------------------

eda = plt.figure(figsize=(12, 4))

eda.add_subplot(1, 2, 1)
data[1].plot(kind='kde', c='r')

eda.add_subplot(1, 2, 1)
plt.boxplot(data[1])

plt.show()


# ------------------------------------------------------------
# 5.3 Visualisasi Hubungan Tinggi Badan dan Ukuran Sepatu
# ------------------------------------------------------------

plt.scatter(data[0], data[1])

plt.xlabel('Tinggi Badan')
plt.ylabel('Ukuran Sepatu')
plt.title('Tinggi Badan vs Ukuran Sepatu')

plt.show()


# ------------------------------------------------------------
# 5.4 Menghitung Korelasi Antarvariabel
# ------------------------------------------------------------

data.corr()


# ============================================================
# 6. MENDEFINISIKAN VARIABEL X DAN Y
# ============================================================

# X = Variabel independen (Tinggi Badan)
# Y = Variabel dependen (Ukuran Sepatu)

x = data[0].values.reshape(-1, 1)
y = data[1].values.reshape(-1, 1)


# ============================================================
# 7. MEMBAGI DATA TRAINING DAN DATA TESTING
# ============================================================

# 65% data untuk training
# 35% data untuk testing

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.35
)


# ============================================================
# 8. MEMBUAT MODEL LINEAR REGRESSION
# ============================================================

regressor = linear_model.LinearRegression()


# ============================================================
# 9. MELATIH MODEL (MODEL TRAINING)
# ============================================================

# Model mempelajari hubungan antara tinggi badan dan ukuran sepatu
regressor.fit(x_train, y_train)


# ============================================================
# 10. MENENTUKAN NILAI KOEFISIEN DAN INTERCEPT
# ============================================================

# M = Koefisien regresi (slope)
# b = Intercept (konstanta)

M = regressor.coef_[0][0]
b = regressor.intercept_[0]


# ============================================================
# 11. MENAMPILKAN PERSAMAAN LINEAR REGRESSION
# ============================================================

# Rumus regresi linear: Y = M(X) + b

print("Y = ", round(M, 2), "X + ", round(b, 2), sep="")


# ============================================================
# 12. MENGHITUNG SKOR MODEL
# ============================================================

# Mengukur skor model menggunakan data testing

regressor.score(x_test, y_test)


# ============================================================
# 13. MELAKUKAN PREDIKSI DAN VISUALISASI
# ============================================================

# Melakukan prediksi menggunakan data testing
y_pred = regressor.predict(x_test)

# Menampilkan data aktual dan garis hasil prediksi
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, c='r')

plt.xlabel('Tinggi Badan')
plt.ylabel('Ukuran Sepatu')
plt.title('Tinggi Badan vs Ukuran Sepatu')

plt.show()


# ============================================================
# 14. EVALUASI MODEL LINEAR REGRESSION
# ============================================================

# Menghitung Mean Absolute Error (MAE)
# Mengukur rata-rata selisih absolut antara nilai aktual dan prediksi.

# Menghitung Mean Squared Error (MSE)
# Mengukur rata-rata kuadrat selisih antara nilai aktual dan prediksi.

# Menghitung Median Absolute Error
# Mengukur median dari seluruh selisih absolut nilai aktual dan prediksi.

# Menghitung R2 Score
# Mengukur seberapa baik model menjelaskan variasi data aktual.

print(
    "Mean AE\t\t: ",
    round(sm.mean_absolute_error(y_test, y_pred), 2)
)

print(
    "MSE\t\t: ",
    round(sm.mean_squared_error(y_test, y_pred), 2)
)

print(
    "Median AE\t: ",
    round(sm.median_absolute_error(y_test, y_pred), 2)
)

print(
    "R2\t\t: ",
    round(sm.r2_score(y_test, y_pred), 2)
)


# ============================================================
# 15. MELAKUKAN PREDIKSI DENGAN DATA BARU
# ============================================================

# Menginputkan tinggi badan yang ingin diprediksi
tinggi_badan = 164.5

# Melakukan prediksi ukuran sepatu
y = regressor.predict([[tinggi_badan]])[0][0]

print("Hasil Prediksi :", round(y))


# ============================================================
# 16. MEMBANDINGKAN DATA AKTUAL DAN DATA PREDIKSI
# ============================================================

# Melakukan prediksi kembali menggunakan data testing
y_pred = regressor.predict(x_test)

# Membuat tabel perbandingan hasil prediksi
hasil = pd.DataFrame({
    "Tinggi Badan": x_test.flatten(),
    "Data Aktual": y_test.flatten(),
    "Data Prediksi": np.round(y_pred.flatten())
})

# Menampilkan hasil perbandingan
hasil
