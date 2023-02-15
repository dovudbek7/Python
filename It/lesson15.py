# 1 - synatx errors
# 2 -logical error
# 3 - in-proccess err

import requests
import pprint
from PIL import Image

API = 'TuAZpQoOtt0fnwaztoFw1kH67HkAZ229786QfzBmVw2gBjuZ8DzzWhCW'

def download(q):
    HEADERS = {
        "Authorization" : "TuAZpQoOtt0fnwaztoFw1kH67HkAZ229786QfzBmVw2gBjuZ8DzzWhCW" 
    }
    url = f"https://api.pexels.com/v1/search?query={q}&per_page=1"
    page = requests.get(url=url, headers=HEADERS)
    # print(page.status_code)
    # print(page.text)
    print(page.json())
    print(page.links)
    image_url = response
    
download('apple')

