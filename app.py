from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))  # Model regresi atau klasifikasi

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        barang = request.form["barang"]
        jumlah = float(request.form["jumlah"])

        # Data untuk model ML, misalnya hanya 'jumlah'
        prediksi = model.predict([[jumlah]])  # Contoh: prediksi lama pinjam
        prediction = f"{nama} diperkirakan meminjam selama {prediksi[0]:.2f} hari."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
