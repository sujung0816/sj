import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status() #혹시나 프로그램에 문제가 있으면 바로 종료

soup = BeautifulSoup(res.text, "lxml")
# #attrs는 속성값 모두 출력, td태그에서 클래스가 title인값 모두 출력
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 만화제목+링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

#평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate) 
    total_rates +=float(rate) #a += b 왼쪽 변수에 오른쪽 값을 더하고, 그 결과를 왼쪽 변수에 할당한다. a +=b는 즉 a= a+b를 의미함 
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))
