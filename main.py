import requests, time, re
from bs4 import BeautifulSoup
running = True

while running:
    print("\n")
    raw = input("Player: ").lower().strip()

    result = requests.get(f'https://ameobea.me/osutrack/user/{raw}/')

    src = result.content

    soup = BeautifulSoup(src, "lxml")

    ppString = ""
    rankString = ""
    accString = ""

    links = soup.find_all('a')
    print(links[18].text)

    rankTD = soup.find_all('td')[0]
    ppTD = soup.find_all('td')[1]
    accuracyTD = soup.find_all('td')[2]

    for diarrhea in ppTD:
        if "PP" not in diarrhea:
            ppString += diarrhea
    for pebble in rankTD:
        if "Rank" not in pebble:
            rankString += pebble
    for rrtyui in accuracyTD:
        if "Accuracy" not in rrtyui:
            accString += rrtyui
    print(f'\nPP: {ppString.strip()} \nRank: {rankString.strip()}\nAccuracy: {accString.strip()}')
    print("\n")
    kill = input("Quit? (y/n)")
    killf = kill.lower().strip()
    if killf == "yes" or killf == "y":
        running = False
        exit()
    else:
        time.sleep(1)
