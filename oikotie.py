#!/usr/bin/python3

from bs4 import BeautifulSoup

with open('oikotie.html') as the_file:
    soup = BeautifulSoup(the_file, 'lxml')

cards = soup.findChild('div', class_="cards")

tags = cards.findAll('div', class_="cards__card ng-scope")

# for tag in tags:
#     street_address = tag.findChild('div', class_="ot-card__address").div.text

#     area = tag.findChild('div', class_="ot-card__address").findAll('span')
#     if len(area) > 1:
#         distric = area[0].text
#         city = area[1].text
#     elif len(area) == 1:
#         city = area[0].text
#     else:
#         city = "No info"

#     print("========")
#     print(street_address)
#     print(distric)
#     print(city)
#     print("++++++++")

print(tags[0].findChild('div', class_="ot-card__body"))