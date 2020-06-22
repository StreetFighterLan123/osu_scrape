import requests
from bs4 import BeautifulSoup

raw = input("User: ").lower().strip()

result = requests.get(f'https://ameobea.me/osutrack/user/{raw}/')

src = result.content

soup = BeautifulSoup(src, "lxml")


mydivs = soup.find_all("div")

ppdivs = []
string = ""
my_variable_names_suck = ""
for div in mydivs:
    if "PP" in div.text:
        ppdivs.append(div.text)
        ppTD = soup.find_all('td')[1]
        rankTD = soup.find_all('td')[0]
        #print(poopoo_thing)
        for diarrhea in ppTD:
            if "PP" not in diarrhea:
                string += diarrhea
        for pebble in rankTD:
            if "Rank" not in pebble:
                my_variable_names_suck += pebble
        #print(string)

ppList = string.split()
pp = float(ppList[0])

rankList = my_variable_names_suck.split()
rank = rankList[0]
formatted_pp = "{:,}".format(pp)

print(f'\nPP: {formatted_pp} \nRank: {rank}')

