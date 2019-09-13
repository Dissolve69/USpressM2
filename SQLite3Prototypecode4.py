# In My Ubuntu UsatodayDBTest2.py
# USA today Korea Searching Page 1~4 




import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

titles = []
links = []
dates = []
authors = []
contents = []

# page = requests.get('https://www.usatoday.com/search/?q=Korea')
# soup = BeautifulSoup(page.content, 'html.parser')
# usatoday = soup.select('div.gnt_se_hl')

for page in range(1, 4):

    changepage = "https://www.usatoday.com/search/?q=Korea&page="
    changepage += str(page)
    # print("page = ",changepage)
    page = requests.get(changepage)
    soup = BeautifulSoup(page.content, 'html.parser')
    usatoday = soup.select('div.gnt_se_hl')

    for title in usatoday:

            # 이 화면에서 저자, 날짜 빼오기

        dtby = title.parent.find(attrs={"class": "gnt_se_dtby"})
        if (dtby != None):

            print("=======================================================")
            print("Links:", title.parent.parent.get('href'))
            print("Title:", title.text)
            print("Author:", dtby.get('data-c-by'))
            print("Date:", dtby.get('data-c-dt'))
            print("=======================================================")

            Author = dtby.get('data-c-by')
            ArticleDate = dtby.get('data-c-dt')
            Articlelinks = title.parent.parent.get('href')
            Noapostrophe = title.text.replace("'", "")

            SQL = "INSERT INTO test3 (publisher, date, title, author, links) VALUES" \
                      + "(" + "'USAToday'" + "," + "'" + ArticleDate + "'" + "," + "'" + Noapostrophe + "'" \
                      + "," + "'" + Author + "'" + "," + "'" + Articlelinks + "'" + ")"

            cur.execute(SQL)

    cur.execute("select * from test3")
    rows = cur.fetchall()
    print("If you see the following that means DB Working!")
    print(rows)

conn.commit()
conn.close()



