from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
posts=[
    {
        'id':1,
        'obname':'HTML',
        'Detail':'It is used to create Static web Pages'
    },
    {
       'id':2,
        'obname':'CSS',
        'Detail':'Used to apply styles for the webpage'
    },
    {
        'id':3,
        'obname':'JS',
        'Detail':'Used to provide action for the static a web page'
    }
]
def home(request):
    html=''
    for post in posts:
        html+= f'''
        <a href=\'/{post['id']}/\'><h1>{post['id']}-{post['obname']}</h1></a>
        <p>{post['Detail']}</p>
'''
    return render(request,'posts/home.html',{'posts':posts})

def detail(request,id):
    html=''
    home=reverse('home')
    for post in posts:
        if post['id']==id:
            html+=f'''
            <h1>{post['id']}-{post['obname']}</h1>
            <p>{post['Detail']}</p>
            <a href={home}>Home</a>
             '''
            return HttpResponse(html)
    else:
        return HttpResponseNotFound('The number you have entered is in valid')

def re(request,id):
    url=reverse('detail',args=[id])
    return HttpResponseRedirect(url)