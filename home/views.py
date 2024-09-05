from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name="index.html")

def baidu(request):
    return render(request,template_name="baidu.html")


def info(request):

    #1. 普通的变量
    username = "猿神，岂懂？"


    #2， 字典类型
    book = {'name':"姜维",'xndx':"春林"}
    Genshin = {'114':514}

    #3. 列表
    xnm = [
            {'name':"姜维",'xndx':"春林"},
            {'name':"张开",'xndx':"博伟"},
    ]
    

    #4. 对象
    class Person:
        def __init__(self,realname):
            self.realname = realname

            
    context={
            'username': username,
            'book':book,
            'xnm':xnm,
            'Genshin':Genshin,
            'person':Person("国服姜维"),
    }
    return render(request,template_name="info.html",context=context)



def if_view(request):
    return render(request,template_name='if.html')

def with_view(request):
    context={
          'xnm' : [
            {'name':"姜维",'xndx':"春林"},
            {'name':"张开",'xndx':"博伟"},
        ]
    }
    return render(request,template_name='with.html',context=context)


def url_view(request):
    return render(request,template_name='url.html')


def static_view(request):
    return render(request,template_name='static.html')