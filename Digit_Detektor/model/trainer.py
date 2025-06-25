# model/trainer.py

import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Fungsi untuk melatih model dan menyimpannya ke file
def train_and_save_model():
    # Load dataset digit (8x8 pixel gambar)
    digits = load_digits()
    
    # X = fitur gambar, y = label angka
    X, y = digits.data, digits.target

    # Bagi data menjadi data latih dan uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Gunakan model Logistic Regression
    model = LogisticRegression(max_iter=10000)

    # Latih model dengan data latih
    model.fit(X_train, y_train)

    # Simpan model ke file menggunakan pickle
    with open('data/digits_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Model berhasil dilatih dan disimpan!")

# Fungsi untuk memuat model dari file
def load_model():
    with open('data/digits_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Fungsi untuk memprediksi digit dari data gambar
def predict_digit(model, image_data):
    return model.predict([image_data])[0]

# Jika file ini dijalankan langsung, maka lakukan pelatihan
if __name__ == '__main__':
    train_and_save_model()
