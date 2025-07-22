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


def forecast():
    url = "https://api.open-meteo.com/v1/forecast"


