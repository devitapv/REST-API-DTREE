# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

# Load the model
model = joblib.load(open('DecTree.pkl','rb'))

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)
