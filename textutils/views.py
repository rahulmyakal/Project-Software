from django.http import HttpResponse
from django.shortcuts import render

import re

def index(request):
    return render(request,'index.html')

def analyser(request):
    
    # getting the text from entered in text area 
    djtext = request.POST.get('text','default')

    #These all are the methods of TextUtils
    to_capital = request.POST.get('to_capital','off')
    to_removepunct = request.POST.get('to_removepunct','off')
    to_count_words = request.POST.get('to_count_words','off')
    to_remove_newline = request.POST.get('to_remove_newline','off')
    to_remove_extraspace = request.POST.get('to_remove_extraspace','off')
    to_title = request.POST.get('to_title','off')
    to_swapcase = request.POST.get('to_swapcase','off')
    to_lower = request.POST.get('to_lower','off')


    if to_capital =="on":
          
        captilaisation=""
        for i in djtext:
            captilaisation = captilaisation + i.capitalize()
        params={'purpose':' Do captilaisation','final_text':captilaisation,'to_print_input':djtext}
        return render(request,'analyser.html',params)

    elif to_removepunct == "on":

        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed =""
        for char in djtext:
            if char not in punctuation:
                analysed = analysed + char
        params={'purpose':'To Remove Punctuation','final_text':analysed,'to_print_input':djtext}
        return render(request,'analyser.html',params)

    elif to_count_words == "on":

        lenth = len(djtext)
        params={'purpose':'To Count Total Number Of Words','final_text':lenth,'to_print_input':djtext}
        return render(request,'analyser.html',params)

    elif to_remove_newline == "on":
        analyzed = ""
        for char in djtext:
            analyzed =analyzed + char.strip()
        params={'purpose':'To Remove New Line ','final_text':analyzed,'to_print_input':djtext}
        return render(request,'analyser.html',params)
     
    elif to_remove_extraspace == "on":
        
        anaylzed = re.sub(' +',' ',djtext)
        anaylzed =  djtext.strip() 
        params={'purpose':'To Remove Extra Spaces ','final_text':anaylzed,'to_print_input':djtext}
        return render(request,'analyser.html',params)

    elif to_title == "on":
        title = djtext.title()
        params={'purpose':' Do Title','final_text':title,'to_print_input':djtext}
        return render(request,'analyser.html',params)


    elif to_swapcase == "on":
        title = djtext.swapcase()
        params={'purpose':'Do Swapcase','final_text':title,'to_print_input':djtext}
        return render(request,'analyser.html',params)

    elif to_lower == "on":
        title = djtext.lower()
        params={'purpose':'Do Lower Case','final_text':title,'to_print_input':djtext}
        return render(request,'analyser.html',params)

    else:    
        params = {'purpose':'You nothing selected any methods'}
        return render(request,'analyser.html',params)