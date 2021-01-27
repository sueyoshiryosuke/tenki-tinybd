from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://weather.tsukumijima.net/api/forecast"
    payload = {"city":"130010"}
    tenki_data = requests.get(url, params=payload).json()

    return render_template("template.html",
                          tenki_data=tenki_data)

app.run(debug="True", host='0.0.0.0')
