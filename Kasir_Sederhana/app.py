from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpan data belanja di memori
daftar_belanja = []

@app.route('/')
def index():
    total = sum(item['harga'] for item in daftar_belanja)
    return render_template('index.html', belanja=daftar_belanja, total=total)

@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    harga = int(request.form['harga'])
    daftar_belanja.append({'nama': nama, 'harga': harga})
    return redirect(url_for('index'))

@app.route('/hapus/<int:index>')
def hapus(index):
    if 0 <= index < len(daftar_belanja):
        del daftar_belanja[index]
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    daftar_belanja.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
