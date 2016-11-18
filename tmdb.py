from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import requests

key = '3e7807c4a01f18298f64662b257d7059'
useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.41 Safari/537.1'

def search(movie, year=None, max=None):
    params = {
        'api_key': key,
        'query': movie,
        'include_adult': 'true',
    }
    if year != None:
        data['year'] = year

    headers = {
        'accept': 'application/json',
        'user-agent': useragent
    }
    r = requests.get('http://api.themoviedb.org/3/search/movie', params=params, headers=headers)
    res = r.json()
    if max != None:
        res = res[:5]
    return res['results']
