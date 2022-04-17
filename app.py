from ast import Str
from re import X
import string
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def iris_prediction():
    if request.method == 'GET':
        return render_template("berat.html")
    elif request.method == 'POST':
        print(dict(request.form))
        berat = dict(request.form).values()
        berat = np.array([x for x in berat])
        if berat[0]== 'Male':
            berat[0] = float(1)
        else :
            berat[0] = float(0)
        print(berat[0], berat[1])
        X = [berat[0], berat[1]]
        berat = np.array([float(x) for x in berat])
        model, std_scaler = joblib.load("model-development/beratbaru-using-logistic-regression.pkl")
        # berat = std_scaler.transform(X)
        print(berat)
        result = model.predict([berat])
        # Height = {
        #     '0': Height,

        # }
        result = int(result[0])
        return render_template('berat.html', result=result)
    else:
        return "Unsupported Request Method"


if __name__ == '__main__':
    app.run(port=5000, debug=True)