import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

# rank = #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

# tilte = #old_content > table > tbody > tr:nth-child(2) > td.title > div > a

# star = #old_content > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > div > img

# scores = #old_content > table > tbody > tr:nth-child(2) > td.point

movie = soup.select('#old_content > table > tbody > tr')

#반복문
for movies in movie:
    title = movies.select_one('td.title > div > a')

    if title is not None:
        rank = movies.select_one('td > img')['alt']
        title = movies.select_one('td.title > div > a')
        scores = movies.select_one('td.point')
        print(rank, title.text ,scores.text)

