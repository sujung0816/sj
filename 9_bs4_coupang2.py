import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    
    #광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("  <광고 상품 제외 합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    if "Apple" in name:
        print("  < 애플 제품 제외합니다>  ")
        continue

    
    price = item.find("strong", attrs={"class":"price-value"})
    if price:
        price = price.get_text()
    else:
        price = "가격 없음"

    #리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회
    rate  = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("  <평점 없는 상품 제외합니다>  ")
        continue

    rate_cnt  = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
        # print("리뷰 수", rate_cnt)
    else:
        print("  <평점 수 없는 상품 제외합니다>  ")
        continue

    if float(rate) >= 4.0 and int(rate_cnt) >= 50:
        print (name, price, rate, rate_cnt)


        #time 2:15:30