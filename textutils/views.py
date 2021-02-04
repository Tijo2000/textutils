#I have created this python file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')#variable

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')#variable
    fullcaps =  request.POST.get('fullcaps','off')#variable
    newlineremover = request.POST.get('newlineremover', 'off')  # variable
    extraspaceremover = request.POST.get('extraspaceremover', 'off')  # variable
    print(removepunc)
    print(djtext)

    #Check which checkbox is on
    if removepunc =="on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #Analyse the text
        djtext = analyzed
        #return render(request, 'analyze.html' , params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyse the text
        #return render(request, 'analyze.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyse the text
        #return render(request, 'analyze.html', params)



    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!= "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)

        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        #djtext = analyzed
        # Analyse the text

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!= "on"):
        return HttpResponse("Please select a operation and try again")

    return render(request, 'analyze.html', params)