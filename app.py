from flask import Flask, render_template, request
import fake_news
import webbrowser
from threading import Timer
import graph
import pandas as pd

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred_news = fake_news.fake_result(message)
        print(pred_news)
        return render_template('index.html',prediction = pred_news)
    else:
        return render_template('index.html',prediction = "Oops! Something went wrong!")


@app.route('/sub')
def sub():

    case_table = graph.datafilter()
    pred_table = graph.filter()
    return render_template('sub.html', table1=[case_table.to_html(classes='mytab', index = True, header = "true")],table2 = [pred_table.to_html(classes='mytab', index = True, header = True)])

def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

if(__name__) == "__main__":
    Timer(1, open_browser).start();
    app.run(port = 2000 )
