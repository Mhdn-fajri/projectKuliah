# main.py
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import joblib
from sklearn.datasets import load_digits

# Muat model
model = joblib.load("models/digit_model.pkl")

# Buat canvas gambar
class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deteksi Angka AI")

        self.canvas = tk.Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        tk.Button(self.button_frame, text="Prediksi", command=self.predict).pack(side="left")
        tk.Button(self.button_frame, text="Bersihkan", command=self.clear_canvas).pack(side="left")

        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack()

    def paint(self, event):
        x, y = event.x, event.y
        r = 8
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='black')
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="")

    def predict(self):
        # Resize gambar ke 8x8 (ukuran data latih)
        img_resized = self.image.resize((8, 8))
        img_resized = ImageOps.invert(img_resized)  # Balik warna

        img_array = np.array(img_resized).astype(float)
        img_array = (16.0 * img_array / 255.0).reshape(1, -1)  # Normalisasi seperti MNIST

        prediction = model.predict(img_array)[0]
        self.result_label.config(text=f"Prediksi Angka: {prediction}")

# Jalankan aplikasi
root = tk.Tk()
app = DrawApp(root)
root.mainloop()
