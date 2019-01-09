#!/usr/bin/python3

from bs4 import BeautifulSoup

with open('oikotie.html') as the_file:
    soup = BeautifulSoup(the_file, 'lxml')

cards = soup.findChild('div', class_="cards")

tags = cards.findAll('div', class_="cards__card ng-scope")

for tag in tags:
    street_address = tag.findChild('div', class_="ot-card__address").div.text

    area = tag.findChild('div', class_="ot-card__address").findAll('span')
    if len(area) > 1:
        distric = area[0].text
        city = area[1].text
    elif len(area) == 1:
        city = area[0].text
    else:
        city = "No info"

    house_info = tag.findChild('div', class_="ot-card__body").findAll('section')
    
    house_price = house_info[0].findAll('span')[1].text

    house_area = house_info[0].findAll('span')[2].text
    try:
        house_rooms = house_info[1].text
    except IndexError:
        house_rooms = "No Info"

    try:
        house_type = house_info[2].findAll('span')[0].text
    except IndexError:
        house_type = "No Info"

    try:    
        house_year = house_info[2].findAll('span')[1].text
    except IndexError:
        house_year = "No Info"

    print("========")
    print(street_address)
    print(distric)
    print(city)
    print(house_price)
    print(house_area)
    print(house_rooms)
    print(house_type)§
    print(house_year)
    print("++++++++")

# print(tags[0].findChild('div', class_="ot-card__body").findAll('section')[2].findAll('span'))