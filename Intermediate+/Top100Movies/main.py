# Day 45 - Web Scraping Top 100 Movies

import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/') # noqa
soup = BeautifulSoup(response.text, 'html.parser')

movies = [movie.getText() for movie in soup.find_all(name='h3', class_='title')] # noqa

movies.reverse()

with open('top_movies.txt', 'w', encoding='utf8') as file:
    for movie in movies:
        file.write(movie)
        file.write('\n')
