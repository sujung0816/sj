#네이버 카페 글, 다음 메일 제목 등등 html문서를 가지고 와서 bs를 통해서 재작업
import time
from selenium import webdriver

browser = webdriver.Chrome() #다른파일에 설치했으면 위치 명시 필요 ex ""./chromedriver.exe"

#1. 네이버로 이동
browser.get("https://naver.com")

#2. 로그인 버튼 이동
browser.find_element_by_xpath('//*[@id="account"]/a').click()

#3. id,pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

#5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html정보 출력
print(browser.page_source)

#7. 브라우저 종료
# browser.close() #현재 탭만 종료
browser.quit() #전체 브라우저 종료

# 3:21:53
# 자동방지코드 https://dev-guardy.tistory.com/37

