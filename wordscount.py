
from django.http import HttpResponse
from django.shortcuts import render
import operator

## 소스 코드는 압축적이라 짧아요. 이 프로그램 실행 했을때 결과 화면도 함께 보내드리께요. 

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
