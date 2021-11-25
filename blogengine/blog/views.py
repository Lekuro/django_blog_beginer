from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    print('request ', request)
    print('dir(request)')
    print(dir(request))
    return HttpResponse('<h1>Hello world</h1>')

def blogposts_list(request):
    l=['Anna','Oleg']
    return render(request,'blog/index.html', context={'names':l})
