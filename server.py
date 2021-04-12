from flask import Flask, request, render_template, redirect, url_for
import json
import requests

app = Flask(__name__)

@app.route('/v1/home', methods=['GET'])
def home ():
    return(render_template('index.html'))

@app.route('/v1/about', methods=['GET'])
def about():
    return ("Hello, I am a robot from UBTECH Robotics, nice to meet you")

@app.route('/v1/weather', methods=['GET'])
def weather():
    city = request.args.get('q')
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=dc20d3160e7d504175d202850b79b74b&q='
    base_url = url + city
    response= requests.get(base_url).json()
    #data = response.json()
    description = response["weather"][0]["description"]
    return (render_template('index.html', city=city, weather = description))


if __name__ == '__main__':
    app.run(host='192.168.1.6', port=8888, debug=True)
