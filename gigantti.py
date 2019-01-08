from bs4 import BeautifulSoup

with open('source_page.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

containers = soup.find_all("div", class_="mini-product")

file_name = "gigantti_puhelin.csv"

f = open(file_name, "w")
headers = "Product name, Selling price, Normal price, Amount in stock\n"

f.write(headers)

for container in containers:
    product_name = container.findChild('a', class_="product-name")['title']

    selling_price = container.findChild('div', class_="product-price").text

    normal_price_tag = container.findChild('div', class_="mini-product-content").findChild('span', class_="sales-point")

    if normal_price_tag:
        try:
            normal_price = int(normal_price_tag.text.split()[-1])
        except ValueError:
            normal_price = selling_price
        print(normal_price)
    else:
        normal_price = selling_price
    
    check_amout = container.findChild('div', class_="product-in-stock").span.span
    if check_amout:
        amount_in_stock = check_amout.text.split()[1]
    else:
        amount_in_stock = "Out of Stock"

    f.write("{},{},{},{}\n".format(product_name, selling_price, normal_price, amount_in_stock))

f.close()


