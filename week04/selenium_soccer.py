from selenium import webdriver
from selenium.webdriver.common.by import By
import xlwt

if __name__ == "__main__":
    year = 2017
    month = 8

    driver = webdriver.Chrome()
    driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=")

    # 엑셀파일쓰기
    rownum = 0
    wb = xlwt.Workbook(encoding="utf-8")
    sheet = wb.add_sheet("Sheet1", cell_overwrite_ok=True)
    sheet.write(rownum, 0, "일시")
    sheet.write(rownum, 1, "경기")
    rownum += 1

    for day in range(1, 32):
        input_query = driver.find_element(By.XPATH, "//*[@id='nx_query']")
        input_query.clear()
        input_query.send_keys("{}년 {}월 {}일 k리그 클래식 경기일정".format(year, month, day))
        driver.find_element(By.XPATH, "//*[@id='nx_search_form']/fieldset/button").submit()

        try:
            i = 1
            while True:
                row = driver.find_element(By.CLASS_NAME, "_scroll_content").find_element(By.XPATH, "tr[{}]".format(i))
                time = row.find_element(By.CLASS_NAME, "time").find_element(By.TAG_NAME, "span").text
                team1 = row.find_element(By.CLASS_NAME, "l_team").find_element(By.TAG_NAME, "span").text
                team2 = row.find_element(By.CLASS_NAME, "r_team").find_element(By.TAG_NAME, "span").text

                print("{}년 {}월 {}일 {} {} vs. {}".format(year, month, day, time, team1, team2))

                sheet.write(rownum, 0, "{}년 {}월 {}일 {}".format(year, month, day, time))
                sheet.write(rownum, 1, "{} vs. {}".format(team1, team2))
                i += 1
                rownum += 1
        except:
            pass

    wb.save("test.xls")