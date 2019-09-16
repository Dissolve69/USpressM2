
from django.http import HttpResponse
from django.shortcuts import render
import operator


def count(request):
    
    ###############################  09/17 #################################3
    
    
    # fulltext 이 부분은 승현님이 가져오신 기사 내용이 들어가고요 
    # 승현님은 해당 URL 에서 가져오면 되요
    fulltext = request.GET['fulltext']
    
    # 가져온 기사 내용을 공백을 기준으로 단어로 분류해 리스트 형식으로 만들고요
    # wordlist 안에는 단어가 쪼개져 리스트 형식으로 들어가고 있어요
    wordlist = fulltext.split()
    
    #dictionary 선언 합니다. 파이썬 dictionary 는 {Key:Value} 형식으로 되어 있어요 
    #여기선 해당 기사 내용 {단어:반복수} 로 만들기 위해 선언했어요
    worddictionary = {}

    for word in wordlist:
        # 가져온 기사에서 단어를 분류한 다음 dictionary worddictionary 안에 해당 단어가 없다면 그 단어 Value 값을 1로 놓고
        # 이후로 가져온 단어가 있다면 기존 Value 값에 1씩 더해 해당 단어 반복수를 카운트 하고 있어요
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
            
            
    # sorted 함수를 이용해 worddictionary 값을 정렬하는데 그 기준을 value 로 하겠다는 의미가 key=operator.itemgetter(1) 이고
    # 역순으로 표시 하겠다가 reverse=True 됩니다. 
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    
    # count.html 로 변수값을 보내는데 전체 기사 내용, 그리고 기사 단어를 공백으로 분류해 리스트로 만든 wordlist 를 len 함수를 이용해
    # 총 몇 단어인지 알아내고 있고 마지막으로 dictionary 인 worddictionary 를 sortedwords에 담아 보내고 있어요.  

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

    # 만약 입력 Text 로 아래와 같은 단어들이 연속해서 들어갔다면 
    
    """
    code fair winner code fair winner code fair winner code fair winner 
    code fair winner code fair winner code fair winner code fair winner 
    code fair winner code fair winner code fair winner code fair winner 
    code fair winner code fair winner code fair winner code fair winner code
    """
    # dictioinary 형태인 sortedwords 안에는 {'code': 17, 'fair':16, 'winner': 16} 이 들어가 있어요
    # 단어수를 wordlist 에서 len 을 이용해 얻은 count 안에는 총 단어수인 49 가 있어요. 
 
""" count.html
<h1>Your Text:</h1>
{{ fulltext }} <-- 파이썬에서 받은 전체 텍스트를 보여주고

<h1>Word Count:</h1>
{% for word, counttotal in sortedwords %} <-- sortedwords 는 dictionary 형태라 { key(단어), value(반복수)}  값은 for 문을 돌려 뿌리고 있어요
{{ word }} - {{counttotal}}
<br />
{% endfor %}
<br /><br /><br />

"""
  # 찾아보니 collections 객체를 이용 문자열 단어의 갯스를 셀수 있는데 나중에 선택 사항이고 지금은 이제 코드가 다 이해 되었을거라 생각해요. 
  



     
    






