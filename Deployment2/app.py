import flask
from flask import request
import numpy as np
import pickle

scaler = pickle.load(open('model/scaler.pkl', 'rb'))
model = pickle.load(open('model/model_fp2.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Lokasi = int(request.form['Lokasi'])
    Hari_Ini_Hujan = int(request.form['Hari_Ini_Hujan'])
    Kelembaban_3Sore = float(request.form['Kelembaban_3Sore'])
    Kecepatan_Angin = float(request.form['Kecepatan_Angin'])
    Tekanan_Udara_9Pagi = float(request.form['Tekanan_Udara_9Pagi'])
    predict_list = [[Lokasi, Hari_Ini_Hujan, Kelembaban_3Sore, Kecepatan_Angin,Tekanan_Udara_9Pagi]]
    predict = scaler.transform(predict_list)
    prediction = model.predict(predict)
    output = {0: 'Tidak Hujan', 1: 'Hujan'}
    return flask.render_template('main.html', prediction_text='Prediksi Cuaca Hari Esok yaitu {}'.format(output[prediction[0]]))