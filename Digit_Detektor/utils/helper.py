# utils/helper.py

import matplotlib.pyplot as plt

# Menampilkan gambar digit
def show_digit_image(image):
    plt.gray()                # Tampilkan dalam skala abu-abu
    plt.matshow(image)        # Plot gambar
    plt.title("Gambar Digit yang Akan Diprediksi")
    plt.show()
