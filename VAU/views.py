from django.http import HttpResponse
from django.shortcuts import render


# Code for video 7

def index(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalise = request.POST.get('capitalise', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_[{}]\|;':",./<>?`~'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose' : 'Removed Punctuations' , 'analysed_text': analysed}
        djtext=analysed
        #return render(request,'analyse.html',params)
    if capitalise =="on":
        analysed=""
        for char in djtext:
            analysed=analysed+char.upper()
        params={'purpose' : 'Changed to Uppercase' , 'analysed_text': analysed}
        djtext=analysed
        #return render(request,'analyse.html',params)
    if spaceremove =="on":
        analysed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analysed=analysed+char;
        params={'purpose' : 'Removes Blankspace' , 'analysed_text': analysed}
        djtext = analysed
        #return render(request,'analyse.html',params)
    if newlineremover =="on":
        analysed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analysed=analysed+char;
        params={'purpose' : 'Combines String in a Single Line' , 'analysed_text': analysed}
        djtext = analysed
        return render(request,'analyse.html',params)
    if charcount =="on":
        c: int=0
        d: int=0
        for char in djtext:
            if char!='''!@#$%^&*()_[{}]\|;':",./<>?`~  ''' :
                c=c+1
            if char==' ':
                d=d+1
        params={'purpose' : 'Counts Total Characters' , 'analysed_text': (c-d)}
        #return render(request,'analyse.html',params)
    if removepunc!="on" and capitalise != "on" and spaceremove !="on" and newlineremover !="on" and charcount !="on":
        return HttpResponse("Error! Please select atleast one option.")
    return render(request, 'analyse.html', params)