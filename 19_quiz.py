# #다음 접속
# import time
# from selenium import webdriver

# browser = webdriver.Chrome() 

# browser.get("https://www.daum.net/")

# #2. 검색 커서 클릭
# browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div').click()

# #3. 송파 헬리오시티 입력
# browser.find_element_by_id("q").send_keys("송파헬리오시티")

# #4. 검색버튼 클릭
# browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_raws = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, raw in enumerate(data_raws):
    columns = raw.find_all("td")

    print("=====매물 {}======".format(index+1))
    print("거래: ", columns[0].get_text().strip())
    print("면적: ", columns[1].get_text().strip(),"(공급/전용)")
    print("가격: ", columns[2].get_text().strip(), "(만원)")
    print("동: ", columns[3].get_text().strip())
    print("층: ", columns[4].get_text().strip())



