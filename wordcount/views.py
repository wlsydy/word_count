from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def count(request):
    read_txt=request.GET['text']
    len_txt=len(request.GET['text'])
    count_word={}
    for w in read_txt:
        if w  not in read_txt:
            count_word.setdefault[w]=1
        else:
           count_word.setdefault(w, 0)
           count_word[w]+=1
    sorted_count_word=sorted(count_word.items(),key=lambda w:w[0],reverse=True)
    return render(request,'count.html',{'txt_content':read_txt,'len_txt_value':len_txt,"sorted_word":sorted_count_word})

def about(request):
    return render(request,'about.html')