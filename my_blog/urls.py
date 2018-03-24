"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url,re_path
from article.views import home,detail,test,log,your_name,get_hlr,HssNumListView,hssdestdetail,get_log
from article.models import HSS_NUM


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^test/$', test),
    re_path(r'^log/$', log, name='log'),
    re_path(r'^your-name/$', your_name, name='your_name'),
    re_path(r'^get_hlr/$', get_hlr, name='get_hlr'),
    re_path(r'^get_log/$', get_log, name='get_log'),
    re_path(r'^(?P<id>\d+)/$', detail, name='detail'),
    re_path(r'^numdetail/$', HssNumListView.as_view(), name='hssnum-list'),
    path('getnum/<int:msisdn_no>/', hssdestdetail, name='hssdestdetail'),
]
