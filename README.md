# bookrecommendations_api

Very Basic REST API for book recommendations using content based filtering

Run :

python helper.py (to save indices and vectorizer model)


python api.py (enable host)

Query:

>>>import requests

>>>url='http://127.0.0.1:5000/'

>>>params={'query':'The Great Gatsby'}

>>>response= requests.get(úrl,params)

>>>response.json()
