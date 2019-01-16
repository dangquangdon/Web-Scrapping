#!/usr/bin/python3

from bs4 import BeautifulSoup

with open('oikotie.html') as the_file:
    soup = BeautifulSoup(the_file, 'lxml')

cards = soup.findChild('div', class_="cards")

tags = cards.findAll('div', class_="cards__card ng-scope")

csv_file = open("CSV_oikotie.csv", "w")
headers = "Street Adress, Distric, City, House Price, House Area, Rooms, Type, Year\n"
csv_file.write(headers)

def replace_comma(text):
    if "," in text:
        return text.replace(",",".")
    else:
        return text

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

    # Detail info of the house
    house_info = tag.findChild('div', class_="ot-card__body").findAll('section')
    
    # Top section: Price and Area - First row in the card
    house_price = house_info[0].findAll('span')[1].text
    house_area = house_info[0].findAll('span')[2].text

    # Second and third row in the card, could be only rooms info or house types + year, normally both
    rooms_info = tag.findChild('div', class_="ot-card__body").findChild('div', class_="ot-card__text ng-binding")
    if rooms_info:
        house_rooms = rooms_info.text
    else:
        house_rooms = "No Info"
    
    if len(house_info) > 1:
        if len(house_info[-1].findAll('span')) > 1:
            house_type = house_info[-1].findAll('span')[-2].text  
            house_year = house_info[-1].findAll('span')[-1].text
        else:
            house_type = house_info[-1].findAll('span')[0].text 
            house_year = house_info[-1].findAll('span')[0].text 


    csv_file.write("{}, {}, {},{}, {}, {}, {}, {}\n".format(replace_comma(street_address),
                                                             replace_comma(distric),
                                                             replace_comma(city),
                                                             replace_comma(house_price),
                                                             replace_comma(house_area),
                                                             replace_comma(house_rooms),
                                                             replace_comma(house_type),
                                                             replace_comma(house_year)))

    # print("========")
    # print(street_address)
    # print(distric)
    # print(city)
    # print(house_price)
    # print(house_area)
    # print(house_rooms)
    # print(house_type)
    # print(house_year)
    # print("++++++++")
print("Completed !")
csv_file.close()
# print(tags[9].findChild('div', class_="ot-card__body").findAll('section'))