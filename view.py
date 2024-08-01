from flask import Blueprint, render_template, request
from weather import city_weather

views = Blueprint(__name__, "views")

@views.route('/', methods=["GET", "POST"])
def home():
    weather_info = None
    if request.method == "POST":
        city_name = request.form["city"]
        weather_info = city_weather(city_name)
    return render_template('index.html', weather_info=weather_info)
