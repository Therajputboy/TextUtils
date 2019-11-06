# I HAVE CREATED THIS FILE-ROHIT
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     return render(request,'index.html')
def analyze(request):
    #text recieved
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    exspaceremover = request.POST.get('exspaceremover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed =" "
    #check which checkox is on
    if removepunc == "on":

        #removed the punctuations
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Punctuations removed', 'analyzed': analyzed}

    if(fullcaps == "on"):
        if analyzed != " " :
            text = analyzed
            analyzed = " "

            #converted to the capitals letters.
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Capitals', 'analyzed': analyzed}

    if(newlineremover == "on"):
        if analyzed != " "  :
            text = analyzed
            analyzed = " "

        #removing the new line character

        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'New Line Removed', 'analyzed': analyzed}

    if(exspaceremover =="on"):
        if analyzed != " ":
            text = analyzed
            analyzed = " "
        for index,char in enumerate(text):
            if (text[index]==" " and text[index + 1] ==" "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces removed', 'analyzed': analyzed }
    return render(request, 'analyzed.html', params)




