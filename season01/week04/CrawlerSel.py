import time
from selenium import webdriver
import xlrd
from xlutils.copy import copy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
from selenium.webdriver.common.by import By
import xlwt

# driver로 wiki 접속
driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

for i in range(1, 2):
    driver.get("https://google.com")

    # 엑셀 파일 열기
    wb = xlrd.open_workbook('test.xls')
    sheet = wb.sheet_by_index(0)

    copy_wb = copy(wb)
    copy_sheet = copy_wb.get_sheet(0)

    # 검색 키워드 셀에서 가져오기
    keyword = '비트코인 시세'

    # 구글 검색
    elem = driver.find_element_by_id('lst-ib')

    # 공통
    elem.send_keys(keyword)
    elem.submit()

    ##### 구글 검색 결과 페이지 #####
    try:
        box = driver.find_element_by_xpath("//div[@id='rso']/div[2]/div")
        list = box.find_elements_by_tag_name('h3')
        for item in list:
            # print(item.text)
            if ('CoinGecko' in item.text):
                p = item.find_element_by_tag_name('a')
                p.click()
                break


    except NoSuchElementException:

        box = driver.find_element_by_xpath("//div[@id='rso']/div/div")
        list = box.find_elements_by_tag_name('h3')
        for item in list:
            # print(item.text)
            if ('CoinGecko' in item.text):
                p = item.find_element_by_tag_name('a')
                p.click()
                break

    ##### coingecko 비트코인 시세 정보 페이지  #####
    # 비트코인, BTC
    print("//////////////////////////// " + str(i) + "행을 크롤링중입니다.")
    print("//////////////////////////// " + "궁금해궁금해 : " + keyword)

    try:
        table = driver.find_element_by_tag_name('table')
        tbody = table.find_element_by_tag_name("tbody")
        trs = tbody.find_elements_by_tag_name("tr")

    except NoSuchElementException:
        print(" [예외 발생] 표 없음 ")
        continue

    for tr in trs:
        #비트코인 키워드
        if "비트코인" in tr.text:
            print(tr.text)
            a = ""
            if tr.find_elements_by_tag_name("td"):
                lis = tr.find_elements_by_tag_name("td")
                for li in lis:
                    a = a + "," + li.text
            else:
                o = tr.find_elements_by_tag_name("td")
                a = a + "," + o[0].text

            a = a[1:]
            print(a)
            # a전체 내용 엑셀 입력
            copy_sheet.write(i, 1, a)
        # BTC 키워드
        if "BTC" in tr.text:
            print(tr.text)
            a = ""
            if tr.find_elements_by_tag_name("td"):
                lis = tr.find_elements_by_tag_name("td")
                for li in lis:
                    a = a + "," + li.text
            else:
                o = tr.find_elements_by_tag_name("td")
                a = a + "," + o[0].text

            a = a[1:]
            print(a)
            # a전체 내용 엑셀 입력
            copy_sheet.write(i, 1, a)

    # 저장(덮어쓰기)
    copy_wb.save('test.xls')
