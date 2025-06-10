from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def kalkulator():
    hasil = None
    if request.method == 'POST':
        try:
            angka1 = float(request.form['angka1'])
            angka2 = float(request.form['angka2'])
            operasi = request.form['operasi']

            if operasi == 'tambah':
                hasil = angka1 + angka2
            elif operasi == 'kurang':
                hasil = angka1 - angka2
            elif operasi == 'kali':
                hasil = angka1 * angka2
            elif operasi == 'bagi':
                if angka2 != 0:
                    hasil = angka1 / angka2
                else:
                    hasil = 'Error: Pembagian dengan nol'

        except ValueError:
            hasil = 'Error: Input tidak valid'

    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
