from flask import Flask, jsonify,request
from sklearn import svm
import numpy as np
import pandas as pd
import pickle
 
app = Flask(__name__)
 
@app.route('/')
def ridata_pred():
    #getを変数に入れる
    temp = request.args.get("temp")
    hum = request.args.get("hum")
    dust = request.args.get("dust")
    pressure = request.args.get("pressure")
    
    #modelロード
    temp_model = pickle.load(open("temperature_pred.pkl","rb"))
    hum_model = pickle.load(open("humidity_pred.pkl","rb"))
    dust_model = pickle.load(open("dust_pred.pkl","rb"))
    pressure_model = pickle.load(open("pressure_pred.pkl","rb"))
    
    #dfに格納
    df_temp = pd.DataFrame({'Temperature':[temp]})
    df_hum = pd.DataFrame({'humidity':[hum]})
    df_dust = pd.DataFrame({'PM2.5':[dust]})
    df_pressure = pd.DataFrame({'AirPressure':[pressure]})
    
    #予測,返すのは正常1,異常-1
    temp_pred = temp_model.predict(df_temp)
    hum_pred = hum_model.predict(df_hum)
    dust_pred = dust_model.predict(df_dust)
    pressure_pred = pressure_model.predict(df_pressure)
    
    
    return jsonify({
        'Temperature':int(temp_pred),
        'Humidity': int(hum_pred),
        'PM2.5': int(dust_pred),
        'AirPressure':int(pressure_pred)
        })
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)