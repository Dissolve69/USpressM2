# In my ubuntu USatodayDBTest.py
# In IDE SQLitePrototypecode3.py
# USAtoday 데이타 추출 DB 저장 Prototype Source Code  

from django.http import HttpResponse
from django.shortcuts import render
import operator
import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

page = requests.get('https://www.usatoday.com/search/?q=Korea')
soup = BeautifulSoup(page.content, 'html.parser')

usatoday = soup.select('div.gnt_se_hl')
for title in usatoday:

    if (title.parent.parent.get('href').find("/world/") != -1):
        print("=======================================================")
        print("Links:", title.parent.parent.get('href'))
        print("Title:", title.text)
        #titles.append(title.text)

    # 이 화면에서 저자, 날짜 빼오기
    #print("Source = ", title.parent)
    dtby = title.parent.find(attrs={"class": "gnt_se_dtby"})
    if (dtby != None):
        print("Author:", dtby.get('data-c-by'))
        print("Date:", dtby.get('data-c-dt'))

        print("=======================================================")

        Author = dtby.get('data-c-by')
        ArticleDate = dtby.get('data-c-dt')
        Articlelinks = title.parent.parent.get('href')
        Noapostrophe = title.text.replace("'", "")

        SQL = "INSERT INTO test (publisher, date, title, author, links) VALUES" \
              + "(" + "'USAToday'" + "," + "'" + ArticleDate + "'" + "," + "'" + Noapostrophe + "'" \
              + "," + "'" + Author + "'" + "," + "'" + Articlelinks + "'" + ")"

        cur.execute(SQL)

cur.execute("select * from test")
rows = cur.fetchall()
print("If you see the following that means DB Working!")
print(rows)

conn.commit()
conn.close()
