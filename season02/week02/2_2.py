from selenium import webdriver

# PhantomJS 로 네이버 접근하기
url = "http://www.naver.com/"
# PhantomJS 드라이버 선언
driver = webdriver.PhantomJS()
# 3초간 기다린다.
driver.implicitly_wait(3)
print("기다렸다")
# url 접근
driver.get(url)
# 스크린샷 찍기
driver.save_screenshot("website.png")
driver.quit()


## 네이버 로그인하기
url = "https://nid.naver.com/nidlogin.login"
# PhantomJS 드라이버 선언
driver = webdriver.PhantomJS()
# url 접근
driver.get(url)

e = driver.find_element_by_id("id")
e.clear()
e.send_keys("ID")

e = driver.find_element_by_id("pw")
e.clear()
e.send_keys("password")

submit_btn = driver.find_element_by_css_selector("input.btn_global[type=submit]")
submit_btn.submit()

# 스크린샷 찍기
driver.save_screenshot("naverlogin.png")
driver.quit()

