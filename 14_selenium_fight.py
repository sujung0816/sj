from selenium import webdriver
from selenium.webdriver.common.by import By #프린트값 출력을 해야하는데 로딩 시간이 있으면 로딩 되는 시간만큼만 기다려
from selenium.webdriver.support.ui import WebDriverWait #프린트값 출력을 해야하는데 로딩 시간이 있으면 로딩 되는 시간만큼만 기다려
from selenium.webdriver.support import expected_conditions as EC #expected_conditions가 기니까 그낭 줄여서 EC

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) #url로 이동

#가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

#이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

#다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

#이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [1] -> 다음달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

#제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div').click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) #두번째 괄호에 엘레먼트가 나올때까지 기다려줘
    #성공하면 동작 수행
    print(elem.text)

finally:
    browser.quit()

#첫번째 항공권 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text) #elem이 가지는 텍스트 값 출력