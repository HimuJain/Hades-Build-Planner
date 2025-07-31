import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re

Path("images").mkdir(parents=True, exist_ok=True)

def boonImageScraper(godName):
    r = requests.get(f'https://hades.fandom.com/wiki/{godName}/Boons_(Hades)')
    soup = BeautifulSoup(r.content, 'html.parser')
    if godName == "Chaos":
        boonTable = soup.find_all('table', class_='wikitable')
        for i in range(len(boonTable)):
            if i == 0:
                boonImageElements = (boonTable[i].find_all('td', class_='boonTableName'))
                boonImageDownload("Chaos/Boons", boonImageElements)
            else:
                boonImageElements = (boonTable[i].find_all('td', class_='boonTableName'))
                boonImageDownload("Chaos/Curses", boonImageElements)
    else:
        boonTable = soup.find('table', class_='boonTableSB')
        boonImageElements = (boonTable.find_all('td', class_='boonTableName'))
        boonImageDownload(godName, boonImageElements)


def boonImageDownload(godName, boonImageElements=None):

    boonImageElements = [img.find('a') for img in boonImageElements if img.find('a') is not None]
    # boonImageElements.extract()
    boonImages = [img['href'] if 'href' in img.attrs else None for img in boonImageElements]
    Path(f"images/{godName}").mkdir(parents=True, exist_ok=True)

    for img in boonImages:
        print(img)
        img_data = requests.get(img).content
        # print(img_data)
        with open(f"images/{godName}/{re.sub(r'_I(?=\.png$)', '', img.split('/')[7])}", 'wb') as f:
        # with open(f"images/{godName}/{img.split('/')[7]}", 'wb') as f:
            f.write(img_data)



def main():
    godList = ["Aphrodite", "Artemis", "Athena", "Demeter", "Dionysus", "Ares", "Poseidon", "Zeus", "Hermes", "Chaos"]
    for god in godList:
        boonImageScraper(god)

    r = requests.get('https://hades.fandom.com/wiki/Aphrodite/Boons_(Hades)')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)
    boonTable = soup.find('table', class_='boonTableSB')
    boons = boonTable.find_all('tr')
    boonImageElements = (boonTable.find_all('td', class_='boonTableName'))
    boonImageElements = [img.find('a') for img in boonImageElements if img.find('a') is not None]
    # for image in boonImageElements:
    #     print(image)
    #     print("next \n")
    # for img in boonImageElements:
    #     if 'data-src' in img.attrs:
    #         print(img['data-src'])
    #     elif 'src' in img.attrs:
    #         print(img['src'])
    boonImages = [img['href'] if 'href' in img.attrs else None for img in boonImageElements]
    # print(boonImages)
    # boons.pop(0)  # Remove the header row
    Path("images/Aphrodite").mkdir(parents=True, exist_ok=True)

    for img in boonImages:
        img_data = requests.get(img).content
        # print(img_data)
        with open(f"images/Aphrodite/{re.sub(r'_I(?=\.png$)', '', img.split('/')[7])}", 'wb') as f:
        # with open(f"images/Aphrodite/{img.split('/')[7]}", 'wb') as f:
            f.write(img_data)






if __name__ == "__main__":
    main()