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

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text()) #rank1에서 a 태그에 속하는것들에서 텍스트만 뽑아와
# print(rank1.next_sibling) rank1의 다음 값을 가져와
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling #이전 올라가는 함수
# print(rank2.a.get_text())
# print(rank1.parent) #1:22:28
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) #sibling에서 s만 붙이면 형제들 모두 출력

# webtoon = soup.find("a",text="바른연애 길잡이-125")
# print(webtoon)
#soup모든 정보 중 elementary가 a이고 text가 이거인 것을 찾아줘.
