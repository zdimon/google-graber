import requests
url = 'https://www.google.com/search?num=100&nl=en&start=0&tbs=&q=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0+%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2&gws_rd=ssl'
res = requests.get(url)

print(res.text)