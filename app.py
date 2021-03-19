# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:47:46 2021

@author: Tamilvannan
"""



from flask import Flask, render_template, request

import pandas as pd





app = Flask(__name__)

df = pd.read_json('imdbsam.json')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['post'])
def predict():
    prediction = ' '
    feature = [x for x in request.form.values()]
    feature = feature[0]
    final_feature = feature
    for i in df['name']:
        if str(i).lower() != 'none':
            if str(final_feature).lower() == str(i).lower():
                prediction = 'name'
    for j in df['city']:
        if str(j).lower() != 'none':
            if str(final_feature).lower() == str(j).lower():
                prediction = 'city'
    output = prediction
    return render_template('index.html', predict_text='Result  {}' .format(output))





if __name__ == '__main__':
    app.run(debug=True)

