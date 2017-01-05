from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import Article

def home(request):
    post_list = Article.objects.all()  
    return render(request, 'home.html', {'post_list' : post_list})
    
'''
def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
'''

def detail(request, id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
