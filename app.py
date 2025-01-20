from flask import Flask, render_template, request
from math import exp, factorial

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Ambil input dari form
        interarrival_time = float(request.form['interarrival_time'])  # Waktu antar kedatangan (dalam menit)
        service_time = float(request.form['service_time'])  # Waktu pelayanan per pelayan (dalam menit)

        # Hitung λ dan μ
        arrival_rate = 60 / interarrival_time  # λ (Laju kedatangan per jam)
        service_rate = 60 / service_time  # μ (Laju pelayanan per pelayan per jam)

        # Hitung Pemanfaatan Pelayan (ρ)
        rho = arrival_rate / service_rate

        # Hitung Waktu Rata-rata dalam Sistem (W) dan Antrian (Wq)
        w = 1 / (service_rate - arrival_rate)  # Waktu rata-rata dalam sistem
        wq = w - (1 / service_rate)  # Waktu rata-rata dalam antrian

        # Kirim hasil ke template
        return render_template('result.html', 
                               arrival_rate=arrival_rate, 
                               service_rate=service_rate, 
                               rho=rho, 
                               w=w, 
                               wq=wq, 
                               interarrival_time=interarrival_time, 
                               service_time=service_time)

    except ValueError:
        return render_template('result.html', error="Masukkan nilai yang valid!")

if __name__ == '__main__':
    app.run(debug=True)