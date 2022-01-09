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

class NewsBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.search_url= "https://www.google.com/search?tbm=nws&q="
        self.news_text = ""
        self.splt = []

    def kill(self):
        self.driver.quit()

    def refresh(self):
        pw.key_press_once("f5")


    def scrap_news(self, id, ps, keyword ):
        # 구글에서 뉴스를 검색합니다.
        self.driver.get(self.search_url + keyword)
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
        self.news_text = pc.paste()

        # 뉴스 텍스를 스플릿 하빈다.
        self.splt = self.news_text.split("\r\n\r\n")[2:-2]

        # 트위터에 접속합니다.
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        # 아이드를 입력합니다.
        pw.typing(id)

        # 탭 키를 칩니다.
        pw.key_press_once("tab")

        # 비밀번호를 입력합니다.
        pw.typing(ps)

        # 엔터키를 칩니다.
        pw.key_press_once("enter")
        time.sleep(5)

        for el in self.splt:
            # 트위터에 글을 올립니다.
            # 게시물 작성 페이지로 이동
            self.driver.get("https://twitter.com/intent/tweet")
            time.sleep(2)
            pw.type_in(el)
            time.sleep(2)

            # Ctrl + enter 누르기
            pw.key_on("control")
            pw.key_on("enter")
            pw.key_off("control")
            pw.key_off("enter")

            time.sleep(8)



