"""
Author: Jeonghoon Lee
Last Modification: 2022.01.09
https://github.com/Benjijeffdad/twitter_news_macro
"""

import sys
from selenium import webdriver
import pywinmacro as pw
import pyperclip as pc
import time


# 아이드를 입력받습니다.
id = sys.argv[1].strip()

# 패스워드를 입력받습니다.
ps = sys.argv[2].strip()

# 검색어를 입력받습니다.
keyword = sys.argv[3].strip()

# 크롬 드라이버를 불러옵니다.
driver = webdriver.Chrome(executable_path="chromedriver.exe")

# 구글 뉴스 검색 url을 정리합니다.
search_url= "https://www.google.com/search?tbm=nws&q="

# 구글에서 뉴스를 검색합니다.
driver.get(search_url + keyword)
time.sleep(5)

# 클릭할 좌표를 클릭합니다.
location = (902, 199)

# 화면을 클릭합니다.
pw.click(location)

# Ctrl + A를 누릅니다.
pw.ctrl_a()

# Ctrl + C를 누릅니다.
pw.ctrl_c()

# 클립보드의 내용물을 봅아옵니다.
news_text = pc.paste()

# 뉴스 텍스를 스플릿 하빈다.
splt = news_text.split("\r\n\r\n")[2:-2]

# 트위터에 접속합니다.
driver.get("https://twitter.com/login")

# 아이드를 입력합니다.
pw.typing(id)

# 탭 키를 칩니다.
pw.key_press_once("tab")

# 비밀번호를 입력합니다.
pw.typing(ps)

# 엔터키를 칩니다.
pw.key_press_once("enter")
time.sleep(5)

for el in splt:
    # 트위터에 글을 올립니다.
    # 게시물 작성 페이지로 이동
    driver.get("https://twitter.com/intent/tweet")
    time.sleep(2)
    pw.type_in(el)
    time.sleep(2)

    # Ctrl + enter 누르기
    pw.key_on("control")
    pw.key_on("enter")
    pw.key_off("control")
    pw.key_off("enter")

    time.sleep(8)


