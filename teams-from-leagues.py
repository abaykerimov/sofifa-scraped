from bs4 import BeautifulSoup as bs
import requests
import re
import json

def soup_maker(url):
    r = requests.get(url)
    markup = r.content
    soup = bs(markup, 'lxml')
    return soup


data = []


def find_all_teams(soup):
    table = soup.find('table', {'class': 'table-hover'})
    tbody = table.find('tbody')
    items = tbody.find_all('tr')
    for item in items:
        team_id = item.findAll('a')[0].get('href').replace('/team/', '')
        titles = item.findAll('a')[0].text.replace("'", "")
        # print titles

        team = {
            'id': team_id,
            'title': titles
        }

        data.append(team)

        with open('teams.json', 'w') as outfile:
            json.dump(data, outfile)


league_ids = [1,4,7,10,13,14,16,17,19,20,31,32,39,41,50,53,54,56,60,61,63,65,66,67,68,78,80,83,189,308,319,322,332,335,336,341,347,349,350,351,353,2076]

for league in league_ids:
    url = 'https://sofifa.com/league/'+str(league)
    print url
    soup = soup_maker(url)
    find_all_teams(soup)
#
# offset = 0
#
# for i in xrange(0, 600, 80):



# url = 'https://sofifa.com/teams/club?v=18&e=158855&set=true&offset=' + str(offset)
# # print url
# soup = soup_maker(url)
# find_all_teams(soup)
