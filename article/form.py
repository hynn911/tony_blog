from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class HLRForm(forms.Form):
    Usernum = forms.CharField(max_length=100)
    isImsi = forms.BooleanField(required=False)

class LogForm(forms.Form):
    Usernum = forms.CharField(max_length=100)
    # isImsi = forms.BooleanField(required=False)
    BegMounth = forms.CharField(max_length=100)
    EndMounth = forms.CharField(max_length=100)