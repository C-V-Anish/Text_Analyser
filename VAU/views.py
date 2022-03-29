from django.http import HttpResponse
from django.shortcuts import render


# Code for video 7

def index(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalise = request.GET.get('capitalise', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_[{}]\|;':",./<>?`~'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose' : 'Removed Punctuations' , 'analysed_text': analysed}
        return render(request,'analyse.html',params)
    elif capitalise =="on":
        analysed=""
        for char in djtext:
            analysed=analysed+char.upper()
        params={'purpose' : 'Changed to Uppercase' , 'analysed_text': analysed}
        return render(request,'analyse.html',params)
    elif spaceremove =="on":
        analysed=""
        for char in djtext:
            if char!=" ":
                analysed=analysed+char;
        params={'purpose' : 'Removes Blankspace' , 'analysed_text': analysed}
        return render(request,'analyse.html',params)
    elif newlineremover =="on":
        analysed=""
        for char in djtext:
            if char!="\n":
                analysed=analysed+char;
        params={'purpose' : 'Combines String in a Single Line' , 'analysed_text': analysed}
        return render(request,'analyse.html',params)
    elif charcount =="on":
        c: int=0;
        d: int=0;
        for char in djtext:
            if char!='''!@#$%^&*()_[{}]\|;':",./<>?`~  ''' :
                c=c+1;
            if char==' ':
                d=d+1;
        params={'purpose' : 'Counts Total Characters' , 'analysed_text': (c-d)}
        return render(request,'analyse.html',params)
    else:
        return HttpResponse("Error")