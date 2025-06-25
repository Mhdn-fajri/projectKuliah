# main.py
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import joblib
import matplotlib.pyplot as plt
import cv2

# Muat model
model = joblib.load("models/digit_model.pkl")

# Aplikasi GUI
class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deteksi Angka AI")

        # Canvas
        self.canvas_size = 280
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        # Gambar putih
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Bind mouse
        self.canvas.bind("<B1-Motion>", self.paint)

        # Tombol
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🧠 Prediksi", command=self.predict).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🧹 Bersihkan", command=self.clear_canvas).pack(side="left", padx=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 20))
        self.result_label.pack()

    def paint(self, event):
        x, y = event.x, event.y
        r = 10  # radius kuas besar
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='black', outline='black')
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="")

    def preprocess_image(self, img):
        # Ubah ke array, invert warna (angka jadi putih di atas hitam)
        img = ImageOps.invert(img)
        img = np.array(img)

        # Crop bagian gambar yang ada tulisan
        coords = cv2.findNonZero((img < 255).astype(np.uint8))
        x, y, w, h = cv2.boundingRect(coords)

        img_cropped = img[y:y + h, x:x + w]

        # Resize ke 8x8
        img_resized = cv2.resize(img_cropped, (8, 8), interpolation=cv2.INTER_AREA)

        # Normalisasi ke rentang 0–16 seperti data latih
        img_normalized = 16 * (img_resized / 255.0)
        return img_normalized.reshape(1, -1)

    def predict(self):
        img_processed = self.preprocess_image(self.image)

        # Prediksi
        prediction = model.predict(img_processed)[0]
        self.result_label.config(text=f"Prediksi: {prediction}")

        # Tampilkan visual input yang dikirim ke model
        plt.imshow(img_processed.reshape(8, 8), cmap='gray')
        plt.title(f"Input ke Model AI (8x8)")
        plt.show()


# Jalankan
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()
