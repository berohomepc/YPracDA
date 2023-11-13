import requests
from bs4 import BeautifulSoup as BS
mother_link = 'https://ubego.ru'
file = open('output.txt', 'w+')

r = requests.get('https://ubego.ru/quests')
html = BS(r.content, 'html.parser')

# print(len(html.find_all('a', class_ = 'card')))
file.write(f'title;city;duration;route;price')

for el in html.select('.rows > .cards'):
    title = el.select('app-quest-card > .card > .card-body > .card-title')[0].text
    city = el.select('app-quest-card > .card > .card-img-top > .city-name')[0].text
    info = el.select('app-quest-card > .card > .card-footer > .info > tbody > tr > td')
    duration = info[0].text
    route = info[1].text
    price = info[2].text
    file.write(f'{title};{city};{duration};{route};{price}\n')