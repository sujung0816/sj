#headless는 매번 브라우저를 직접 띄울 필요 없이, 서버에서 웹 스크래핑 작업을 할 때 사용.
#크롬을 띄우지 않고 크롬을 쓸 수 있는.

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") #1920X1080크기에 맞춰 브라우저 오픈
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

#headless를 쓸때 user-agent를 바꿔야하는 경우도 때로 있음

