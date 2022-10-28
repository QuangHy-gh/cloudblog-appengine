import os
from urllib import request
import requests


def get_cloudapi_data():
    url = "https://cloudblog-api.uc.r.appspot.com/api/"
    r = requests.get(url)
    hitcount = r.json()
    return hitcount


# <p> {% get_hit_count for postdetail %} views</p>
