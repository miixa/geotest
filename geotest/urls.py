"""geotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from geotest import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/subject', views.subject_view),
    url(r'^test/addsubject',views.addSubject_view),
    url(r'^test/theme/(?P<subject_id>\d+)',views.theme_view),
    url(r'^test/addtheme/(?P<subject_id>\d+)',views.addTheme_view),
    url(r'^test/question/(?P<subject_id>\d+)/(?P<theme_id>\d+)',views.question_view),
    url(r'^test/addquestion/(?P<subject_id>\d+)/(?P<theme_id>\d+)',views.addQuestion_view),
    url(r'^test/answer/(?P<subject_id>\d+)/(?P<theme_id>\d+)/(?P<question_id>\d+)',views.answer_view),
    url(r'^test/addanswer/(?P<subject_id>\d+)/(?P<theme_id>\d+)/(?P<question_id>\d+)', views.addAnswer_view),
    url(r'^tested/$',views.tested_choice_sub),
    url(r'^tested/(?P<subject_id>\d+)',views.tested_view),
    url(r'^tested/calculate',views.write_res_view),
    url(r'^settingtest/(?P<subject_id>\d+)',views.setting_test),
    url(r'^login/', views.view_login),
    url(r'',views.index),
]
