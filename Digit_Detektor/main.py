# main.py

# Mengimpor fungsi load_model dan predict_digit dari trainer
from model.trainer import load_model, predict_digit
from utils.helper import show_digit_image
from sklearn.datasets import load_digits

# Load dataset digits
digits = load_digits()

# Pilih satu sample (misalnya index ke-100)
index = 100
image = digits.images[index]
data = digits.data[index]

# Menampilkan gambar digit
show_digit_image(image)

# Load model yang sudah dilatih
model = load_model()

# Prediksi angka berdasarkan data input
prediction = predict_digit(model, data)

print(f"Model memprediksi angka tersebut adalah: {prediction}")
