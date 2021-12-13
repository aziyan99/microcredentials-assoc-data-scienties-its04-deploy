from flask import Flask, render_template, request, jsonify
import pickle
import sklearn


app = Flask(__name__)


model = pickle.load(open('./models/model.regr', 'rb'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/predict', methods=['POST'])
def predict():
    pintu = request.form['pintu']
    bulan = request.form['bulan']
    model_res = model.predict([[int(pintu), int(bulan)]])
    res = {
        'status': 'success',
        'prediction': model_res[0][0]
    }
    return jsonify(res)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
