from django.core.mail import send_mail

from article.models import Article,HSS_NUM,NumForm
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect

from .form import NameForm,ContactForm,HLRForm
# Create your views here.
def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})
def test(request):

    return render(request, 'test.html', {'current_time':datetime.now()})
def log(request):

    return render(request, 'log.html', {'current_time':datetime.now()})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("xujiinlei")
        form = HLRForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HLRForm()

    return render(request, 'name.html', {'form': form})
def your_name(request):
    Usernum = request.POST.get('Usernum')
    return HttpResponseRedirect('/getnum/'+Usernum+'/')
def getnum(request, num):
    try:
        post = HSS_NUM.objects.get(MSISDN_NO=num)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'getnum.html', {'post' : post})
    # raise post
