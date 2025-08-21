from flask import Flask, render_template
from locations import locations

app = Flask(__name__)


def get_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,relative_humidity_2m_max",
        "hourly": "temperature_2m,wind_speed_10m,precipitation,cloudcover,relative_humidity_2m",
        "timezone": "auto"
    }
    # response = requests.get(url, params=params)


@app.route("/")
def index():
    forecasts = {}
    for name, coords in locations.items():
        forecasts[name] = get_forecast(coords["lat"], coords["lon"])
    return render_template("index.html", forecasts=forecasts)


if __name__ == "__main__":
    app.run(debug=True)

