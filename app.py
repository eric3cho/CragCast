from flask import Flask, render_template

app = Flask(__name__)


def get_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly:" "temperature_2m,wind_speed_10m,precipitation,cloudcover"
        "daily": ""
        "timezone": "auto"
    }


@app.route("/")
def index():
    forecasts = {}
    for name, coords in locations.items():
        forecasts[name] = get_forecast(coords["lat"], coords["lon"])
    return render_template("index.html", forecasts=forecasts)


if __name__ == "__main__":
    app.run(debug=True)

