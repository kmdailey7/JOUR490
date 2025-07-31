import requests, json
METEXT=requests.get('https://datacatalog.cookcountyil.gov/resource/cjeq-bs86.json?$limit=999999').text
data=json.loads(METEXT)
