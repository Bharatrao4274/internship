from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')

link = 'https://medium.com/towards-artificial-intelligence/archive/2015'
soup_ = BeautifulSoup(requests.get(link).text, 'html.parser')
articles = soup_.find_all('div', class_='streamItem streamItem--postPreview js-streamItem')




https://www.dineout.co.in/bangalore-restaurants

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


import requests
from bs4 import BeautifulSoup
import json


def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)

