from django.core.mail import send_mail

from article.models import Article,HSS_NUM,NumForm,HssUser
from article.GetLog import getHwssLogDetail
from datetime import datetime
from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView,RedirectView

from .form import NameForm,LogForm,HLRForm
from django.utils import timezone

def hssdestdetail(request, msisdn_no):
    try:
        post = HssUser.objects.get(msisdn_no=msisdn_no)
    except HssUser.DoesNotExist:
        raise Http404
    return render(request, 'hssnumpost.html', {'post' : post})

class HssNumListView(ListView):

    model = HssUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
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

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("xujiinlei")
        form = LogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogForm()

    return render(request, 'log.html', {'form': form})

def get_hlr(request):
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
    if (not request.POST.get('isImsi')):
        if(not Usernum.startswith("86")):
            Usernum = "86" + Usernum
        Usernum = Usernum[:9]
    else:
        Usernum = Usernum[:10]
    num = int(Usernum)
    try:
        if(request.POST.get('isImsi')):
            post = HssUser.objects.get(imsi_no=num)
        else:
            post = HssUser.objects.get(msisdn_no=num)
    except HssUser.DoesNotExist:
        raise Http404
    return render(request, 'hssnumpost.html', {'post' : post})
def get_log(request):
    Usernum = request.POST.get('Usernum')
    if (not request.POST.get('isImsi')):
        if(not Usernum.startswith("86")):
            Usernum = "86" + Usernum
    # num = int(Usernum)
    bMth = int(request.POST.get('BegMounth'))
    eMth = int(request.POST.get('EndMounth'))
    dMth = 1
    if(bMth > 0 and bMth <= 12 and eMth <= 12):
        if(eMth > 0 and bMth <= eMth):
            dMth = eMth - bMth + 1
    try:
        post_list = getHwssLogDetail(Usernum,str(bMth),str(dMth))
    except HssUser.DoesNotExist:
        raise Http404
    return render(request, 'hwhsslogdetail.html', {'post_list' : post_list})
def getnum(request, num):
    try:
        post = HSS_NUM.objects.get(MSISDN_NO=num)
    except HSS_NUM.DoesNotExist:
        raise Http404
    return render(request, 'hssnumpost.html', {'post' : post})
    # raise post
