# Web Scrapping Project

## Description:  
This project is an exercise project of the Python Course from The Shortcut. The purpose is to let participants to learn and practise Python and web scrapping.
- This project uses [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- Data is collected from [Gigantti website with search keyword "puhelin"](https://www.gigantti.fi/catalog/puhelimet-ja-gps/fi-puhelimet/puhelimet) and [Oikotie](https://asunnot.oikotie.fi/myytavat-asunnot?pagination=1&previousSearchId=1&cardType=100)
- As Gigantti is using infinite scrolling effect, and Oikotie is built with React, we use [Selenium] to automatically open the page, wait for it to render and collect to source HTML
- Later, the data collected will be save in a ```.csv``` file

## Installation:  

To install dependencies  

```
pip install -r requirements.txt
```

Install [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.45/):  

- if you have problems on Mac, maybe follow this [tutorial](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/) 

- TODO: test ChromeDriver installation on Windows and Linux

## How it works:
**Gigantti**
- Navigate to ```gigantti``` folder
- run ```python gigantti_get_source.py``` (it will automatically open your web browser - Chrome, and does its job. Let it run until you see ```Completed!``` in the terminal)
- run ```python gigantti.py``` until it finishes
- open ```gigantti_puhelin.csv``` file to see the results

**Oikotie**
- Navigate to ```oikotie``` folder
- run ```python oikotie_get_html_source.py``` (it will automatically open your web browser - Chrome, and does its job. Let it run until you see ```Completed!``` in the terminal)
- run ```python oikotie.py``` until it finishes
- open ```CSV_oikotie.csv``` file to see the results