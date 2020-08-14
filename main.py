import requests, time, re
from bs4 import BeautifulSoup
running = True

while running:
    print("\n")
    raw = input("Player: ").lower().strip()

    result = requests.get(f'https://ameobea.me/osutrack/user/{raw}/')

    src = result.content

    soup = BeautifulSoup(src, "lxml")

    divs = soup.find_all("div")

    string = ""
    my_variable_names_suck = ""
    bruh_momento = ""
    for div in divs:
        if "PP" in div.text:
            rankTD = soup.find_all('td')[0]
            ppTD = soup.find_all('td')[1]
            accuracyTD = soup.find_all('td')[2]
            for diarrhea in ppTD:
                if "PP" not in diarrhea:
                    string += diarrhea
            for pebble in rankTD:
                if "Rank" not in pebble:
                    my_variable_names_suck += pebble
            for rrtyui in accuracyTD:
                if "Accuracy" not in rrtyui:
                    bruh_momento += rrtyui
        #print(string)

    ppList = string.split()
    pp = float(ppList[0])
    formatted_pp = "{:,}".format(pp)

    rankList = my_variable_names_suck.split()
    rank = rankList[0]

    accuracyList = bruh_momento.split()
    accuracy = accuracyList[0]
    print(f'\nPP: {formatted_pp} \nRank: {rank}\nAccuracy: {accuracy}')
    print("\n")
    kill = input("Quit? (y/n)")
    killf = kill.lower().strip()
    if killf == "yes" or killf == "y":
        running = False
        exit()
    else:
        time.sleep(1)
