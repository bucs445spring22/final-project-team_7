import json
import requests

def request_to_dict(url) -> dict:
    return json.loads(requests.get(url).text)
