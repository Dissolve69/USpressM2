
from django.http import HttpResponse
from django.shortcuts import render
import operator
import requests
from bs4 import BeautifulSoup



def homepage(request):

    # HTML 화면으로 파이썬 변수 값 개별적 넘길때 필요
    titles = []
    links = []
    dates = []
    authors = []
    contents = []

    # 리스트 안 리스트 형식으로 묶어서 출력할때 필요
    USAtodays =[]

    # USAtodays Start Here
    USAtodayspage = requests.get('https://www.usatoday.com/search/?q=Korea')
    USAtodayssoup = BeautifulSoup(USAtodayspage.content, 'html.parser')

    usatoday = USAtodayssoup.select('div.gnt_se_hl')
    for title in usatoday:
        #if (title.parent.parent.get('href').find("/world/") != -1):
          #print("=======================================================")

        # 이 화면에서 저자, 날짜 빼오기
        #print("Source = ", title.parent)
        dtby = title.parent.find(attrs={"class": "gnt_se_dtby"})
        if (dtby != None):
           # print("Author:", dtby.get('data-c-by'))
           # print("Date:", dtby.get('data-c-dt'))

           # print("=======================================================")

            Author = dtby.get('data-c-by')
            ArticleDate = dtby.get('data-c-dt')
            Articlelinks = title.parent.parent.get('href')
            # DB SQL 입력할때 Title 내에서 ' 삭제 Noapostrophe
            # Noapostrophe = title.text.replace("'", "")

            USAtodays.append([ArticleDate, title.text, Author, Articlelinks])

            #titles.append(title.text)
            #dates.append(ArticleDate)
            #authors.append(Author)
            #links.append(Articlelinks)

    # return render(request, 'home.html', {'titles': titles,'dates': dates, 'links': links, 'authors': authors})

    # USAtodays End Here

    # 다른 언론사 정보도 리스트 안 리스트 형식으로 HTML 전달
    return render(request, 'home.html', {'USAtodays': USAtodays})
