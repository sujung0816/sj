import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
ranks = soup.find("ol", attrs={"id":"realTimeRankFavorite"}).find_all("li")
for rank in ranks:
    print(rank.get_text().strip())