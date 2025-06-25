# train_model.py
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset angka
digits = load_digits()
X, y = digits.data, digits.target

# Bagi data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Simpan model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/digit_model.pkl")
print("✅ Model berhasil disimpan.")
