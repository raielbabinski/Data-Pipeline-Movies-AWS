import requests
import pandas as pd
from IPython.display import display


url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": ""
}

response = requests.get(url, headers=headers)
data = response.json()

results = data["results"]

df = pd.DataFrame(results)
print(df.columns)