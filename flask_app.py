

# Import Libraries
from flask import Flask, request, jsonify
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Load the model
model = joblib.load(open('/home/Devitapv/mysite/DecTree.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    dataa = request.get_json(force=True)

    predi = []
    for data in dataa:
        # Menghitung prediksi berdasarkan dataset
        prediction = model.predict([np.array([data['MARRIAGE'],data['EDUCATION'],data['SEX']])])

        # Hasil Prediksi
        output = float(prediction[0])
        results = 'Customer diprediksi TERLAMBAT melakukan pembayaran bulan selanjutnya' if output==1 else 'Customer diprediksi TIDAK TERLAMBAT melakukan pembayaran bulan selanjutnya'
        predi.append(results)
    return jsonify(predi)