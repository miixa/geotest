from django.forms import ModelForm
from geotest.models import *
from django import forms

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ['title', 'subject']

class addQuestionForm(forms.Form):
    subject = forms.CharField(label="Предмет", max_length=20)
    theme = forms.CharField(label="Тема", max_length=20)
    question = forms.CharField(label="Вопрос", max_length=20)
    coranswer = forms.CharField(label="Правильный ответ", max_length=20)
    incoranswer = forms.CharField(label="Не правильный ответ", max_length=20)





#class AddCarForm (forms.Form):
#    Number = forms.CharField(label="Номер машины",max_length=9)
#    Model = forms.CharField(label="Марка машины",max_length=50)
#    FIO = forms.CharField(label="Ф.И.О водителя",max_length=100)
#    Phone = forms.CharField(label="телефон водителя",max_length=12)
#    InDate = forms.DateField(label="дата вЪезда", widget=html5_widgets.DateInput(format='%Y.%m.%d'))
#    InTime = forms.TimeField(label="Время въезда",widget=html5_widgets.TimeInput(format='%H:%M'))
#    invoce = forms.FileField(label="invoce")
#    tir = forms.FileField(label="TIR")
#    cmr = forms.FileField(label="CMR")
#    declaration = forms.FileField(label="Декларация")
#    gd = forms.FileField(label="ГД")
#    buh = forms.FileField(label="Бухгалтерские документы")
#    OtherDocument = forms.FileField(label="Другие документы")
#    OutTime = forms.TimeField(label="Время выезда",widget=html5_widgets.TimeInput(format='%H:%m'))
#    OutDate = forms.DateField(label="дата выезда",widget=html5_widgets.DateInput(format='%Y.%m.%d'))
