from bs4 import BeautifulSoup as bs
import requests
import json


def soup_maker(url):
    r = requests.get(url)
    markup = r.content
    soup = bs(markup, 'lxml')
    return soup


data = []


def find_all_players(soup):
    table = soup.find('table', {'class': 'table-hover'})
    tbody = table.find('tbody')
    items = tbody.find_all('tr')
    for item in items:
        id = item.find('img').get('id')
        titles = item.findAll('a')[1].get('title').replace("'", "")
        positions = item.findAll('a')[2].find('span').text
        skills = item.find('div', {'class': 'col-digit col-oa'}).find('span').text
        ages = item.find('div', {'class': 'col-digit col-ae'}).text.strip()
        team = item.findAll('div', {'class': 'col-name text-clip rtl'})[1].find('a').text

        team_id = item.findAll('div', {'class': 'col-name text-clip rtl'})[1].find('a').get('href').replace('/team/', '')
        # print team_id

        player = {
            'id': int(id),
            'title': titles,
            'position': positions,
            'age': int(ages),
            'skill': int(skills),
            'team_id': int(team_id)
        }

        data.append(player)
        # print player
        with open('all_players.json', 'w') as outfile:
            json.dump(data, outfile)


offset = 0

for i in xrange(0, 17600, 80):
    url = 'https://sofifa.com/players?v=18&e=158855&set=true&offset=' + str(offset)
    print url
    offset = i + 80
    soup = soup_maker(url)
    find_all_players(soup)
