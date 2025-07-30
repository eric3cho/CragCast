import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd

# setup cache and retry
# cache_session: store response in cache up to 1 hour
# retry_session: retries up to 5 times, waits 0.2s between retries
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

locations = ["goldbar", "index", "leavenworth", "squamish"]
lat = [47.84769, 47.82481, 47.5967, 49.68218]
lon = [-121.60991, -121.56191, -120.65936, -123.14798]


def forecast():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 47.84769,
        "longitude": -121.60991,
        "hourly": [
            "temperature_2m",
            "wind_speed_10m",
            "precipitation",
            "cloudcover",
            "relative_humidity_2m",
            "weathercode"
        ],
        "forecast_days": 3,
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # process hourly data
    response = responses[0]
    hourly = response.Hourly()
    hourly_data = {
        # "time": hourly.Time(),
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),  # temperature
        "wind_speed_10m": hourly.Variables(1).ValuesAsNumpy(),
        "precipitation": hourly.Variables(2).ValuesAsNumpy(),
        "cloudcover": hourly.Variables(3).ValuesAsNumpy(),
        "relative_humidity_2m": hourly.Variables(4).ValuesAsNumpy(),
        "weathercode": hourly.Variables(5).ValuesAsNumpy()
    }

    df = pd.DataFrame(data=hourly_data)
    print(df.head())




