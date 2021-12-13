from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", hasil=0)


@app.route('/predict', methods=['POST'])
def predict():
    pass
