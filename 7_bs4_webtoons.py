import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() #혹시나 프로그램에 문제가 있으면 바로 종료
soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a",attrs={"class":"title"}) #조건에 해당하는 모든 것을 찾아라.
# class속성이 title인 모든 "a" element를 반환
for cartoon in cartoons: #반복문
    print(cartoon.get_text())