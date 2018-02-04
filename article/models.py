from django.db import models
from django.forms import ModelForm

# Create your models here.
class HSS_NUM(models.Model):
    MSISDN_NO = models.DecimalField(max_digits=20, decimal_places=0, primary_key=True)  # MSISDN号码

    IMSI_NO = models.DecimalField(max_digits=20, decimal_places=0)  # IMSI号码

    HSS = models.CharField(max_length=50, blank=False)  # 归属HSS，严格来说哦，归属HLR

    City = models.CharField(max_length=50, blank=True, null=True)  # 归属城市

    def __unicode__(self):
        return self.MSISDN_NO + ":" + self.HSS

    class Meta:  # 按号段正序排序

        ordering = ['MSISDN_NO']

class Article(models.Model):

    title = models.CharField(max_length = 100) #博客题目

    category = models.CharField(max_length = 100) #博客题目

    category = models.CharField(max_length = 50,blank = True) #博客标签

    date_time = models.DateTimeField(auto_now_add = True) #博客日期

    content = models.TextField(blank = True,null = True) #博客文章正文

    def __unicode__(self):

        return self.title

    class Meta: #按时间下降排序

        ordering = ['-date_time']

class NumForm(ModelForm):
    class Meta:
        model = HSS_NUM
        # fields = ['MSISDN_NO', 'IMSI_NO', 'HSS']
        fields = '__all__'