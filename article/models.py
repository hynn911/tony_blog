from django.db import models
from django.forms import ModelForm

# Create your models here.
class HssUser(models.Model):
    msisdn_no = models.BigIntegerField(db_column='MSISDN_NO', primary_key=True)  # Field name made lowercase.
    imsi_no = models.BigIntegerField(db_column='IMSI_NO', blank=True, null=True)  # Field name made lowercase.
    hss = models.CharField(db_column='HSS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HSS_USER'
    def __unicode__(self):
        return self.MSISDN_NO

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

    title = models.CharField(max_length = 100) #题目

    category = models.CharField(max_length = 100) #类别

    date_time = models.DateTimeField(auto_now_add = True) #上线日期

    content = models.TextField(blank = True,null = True) #处理url

    url = models.CharField(max_length = 100) #处理url

    def __unicode__(self):

        return self.title

    class Meta: #按时间下降排序

        ordering = ['-date_time']


class CmdinfoHwhss(models.Model):
    cmd = models.CharField(db_column='CMD', primary_key=True, max_length=64)  # Field name made lowercase.
    cmd_name = models.CharField(db_column='CMD_NAME', max_length=256)  # Field name made lowercase.
    param = models.CharField(db_column='PARAM', max_length=256)  # Field name made lowercase.
    param_name = models.CharField(db_column='PARAM_NAME', max_length=2048)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMDINFO_HWHSS'

    def __unicode__(self):

        return self.cmd_name


class NumForm(ModelForm):
    class Meta:
        model = HSS_NUM
        # fields = ['MSISDN_NO', 'IMSI_NO', 'HSS']
        fields = '__all__'