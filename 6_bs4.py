import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() #혹시나 프로그램에 문제가 있으면 바로 종료

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(suop.a) souo은 모든 html정보를 가지고 있는데 그 중 첫번째로 발견된 a 태그 정보를 뿌려줘
# print(soup.a.attrs) #attrs는 태그 속성을 보여줘
# print(soup.a["href"]) #a element의 href 속성 값을 출력할 수 있다.

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) #a태그에 해당하는 첫번째 엘리먼트를 찾아줘, class값이 "class":"Nbtn_upload"인 a element를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"})) rank 1에 해당하는 모든 값

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)