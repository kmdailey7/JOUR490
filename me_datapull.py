import requests, json
METEXT=requests.get('https://datacatalog.cookcountyil.gov/resource/cjeq-bs86.json?$limit=999999').text
ME_DATA=json.loads(METEXT)
ME_DATA[0]
