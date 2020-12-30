import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls003862365/?sort=list_order,asc&st_dt=&mode=simple&page=1&ref_=ttls_vw_smp'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
films = soup.find_all('div', 'col-title')

for film in films:
    nameOfFilm = film.find('a').contents[0]
    yearOfFilm = film.find('span','lister-item-year').text
    indexOfFilm = film.find('span', 'lister-item-index').text
    filmList =  nameOfFilm + ' ' + yearOfFilm
    # print(filmList)

with open('cagefilms.txt') as films:
    films = films.readlines()
    films = [ line.strip() for line in films]

    # for line in films:
    #     # print(line)