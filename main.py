import requests
from bs4 import BeautifulSoup

raw = input("User: ").lower().strip()

result = requests.get(f'https://ameobea.me/osutrack/user/{raw}/')

src = result.content

soup = BeautifulSoup(src, "lxml")


mydivs = soup.find_all("div")

ppdivs = []
string = ""
for div in mydivs:
    if "PP" in div.text:
        ppdivs.append(div.text)
        poopoo_thing = soup.find_all('td')[1]
        #print(poopoo_thing)
        for diarrhea in poopoo_thing:
            if "PP" not in diarrhea:
                string += diarrhea
        #print(string)

ppList = string.split()
pp = float(ppList[0])

y = "{:,}".format(pp)
print(f'PP: {y}')

