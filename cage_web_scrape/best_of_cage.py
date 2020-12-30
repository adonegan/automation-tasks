import requests
from bs4 import BeautifulSoup
# scrape this URL below
# url contains list of Nicolas Cage's films and misc info
url = 'https://www.imdb.com/list/ls003862365/?sort=list_order,asc&st_dt=&mode=simple&page=1&ref_=ttls_vw_smp'
response = requests.get(url)
# get url/page in lxml format
soup = BeautifulSoup(response.text, 'lxml')
# find everything in this div element
films = soup.find_all('div', 'col-title')
for film in films:
    # loop over each film and find the following:
    # name of film, year it was made, list number
    nameOfFilm= film.find('a').contents[0]
    yearOfFilm = film.find('span','lister-item-year').text
    indexOfFilm = film.find('span', 'lister-item-index').text
    # create new variable containing all three variables/findings
    filmList = indexOfFilm + ' ' + nameOfFilm + ' ' + yearOfFilm
    print(filmList)

# TBC



