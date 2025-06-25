# ================================================
# main.py - Sistem Deteksi Angka Tulisan Tangan
# ================================================

# Import library yang dibutuhkan
import numpy as np  # Untuk operasi numerik
import matplotlib.pyplot as plt  # Untuk visualisasi gambar
from sklearn.datasets import load_digits  # Dataset angka
from sklearn.model_selection import train_test_split  # Untuk membagi data
from sklearn.linear_model import LogisticRegression  # Model AI sederhana
from sklearn.metrics import accuracy_score  # Mengukur akurasi model
import joblib  # Untuk menyimpan dan memuat model

# ------------------------------------------------
# Load dataset digit angka dari sklearn
digits = load_digits()  # Dataset 8x8 pixel gambar angka
X = digits.data  # Fitur (gambar dalam bentuk array)
y = digits.target  # Label (angka 0-9)

# Tampilkan salah satu gambar sebagai contoh
plt.gray()
plt.matshow(digits.images[0])  # Visualisasi gambar pertama
plt.title(f"Contoh Gambar: {y[0]}")
plt.show()

# ------------------------------------------------
# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------------------------
# Melatih model AI sederhana (Logistic Regression)
model = LogisticRegression(max_iter=10000)  # Model klasifikasi
model.fit(X_train, y_train)  # Melatih model dengan data latih

# ------------------------------------------------
# Menguji akurasi model terhadap data uji
y_pred = model.predict(X_test)  # Prediksi
accuracy = accuracy_score(y_test, y_pred)  # Hitung akurasi
print(f"✅ Akurasi model: {accuracy:.2f}")

# ------------------------------------------------
# Menyimpan model ke folder models/
import os
os.makedirs('models', exist_ok=True)  # Buat folder jika belum ada
joblib.dump(model, 'models/digit_model.pkl')  # Simpan model
print("💾 Model disimpan di models/digit_model.pkl")

# ------------------------------------------------
# Prediksi satu gambar dari data uji
index = 10
sample_image = X_test[index].reshape(1, -1)  # Ambil satu gambar
prediction = model.predict(sample_image)  # Prediksi angka
print(f"🔍 Prediksi angka: {prediction[0]}")
plt.matshow(X_test[index].reshape(8, 8))  # Tampilkan gambar
plt.title(f"Model Menebak: {prediction[0]}")
plt.show()
