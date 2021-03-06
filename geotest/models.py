from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(User):
    role = models.CharField(max_length=200)


class Subject(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser)
    # def __unicode__(self):
    # return self.title


class Theme(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject)
    user = models.ForeignKey(CustomUser)
    # def __unicode__(self):
    # return self.title


class Question(models.Model):
    title = models.CharField(max_length=400)
    subject = models.ForeignKey(Subject)
    theme = models.ForeignKey(Theme)
    user = models.ForeignKey(CustomUser)
    # def __unicode__(self):
    # return self.title

class Answer(models.Model):
    title = models.CharField(max_length=400)
    question = models.ForeignKey(Question)
    subject = models.ForeignKey(Subject)
    theme = models.ForeignKey(Theme)
    user = models.ForeignKey(CustomUser)
    result = models.IntegerField()

class results(models.Model):
    uniqid = models.CharField(max_length=20)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    result = models.IntegerField()

#class CorrectAnswer(models.Model):
#   title = models.CharField(max_length=400)
#    question = models.ForeignKey(Question)
#    subject = models.ForeignKey(Subject)
#    theme = models.ForeignKey(Theme)
#    user = models.ForeignKey(CustomUser)
    # def __unicode__(self):
    # return self.title

#class IncorrectAnswer(models.Model):
#    title = models.CharField(max_length=400)
#    question = models.ForeignKey(Question)
#    subject = models.ForeignKey(Subject)
#    theme = models.ForeignKey(Theme)
#    user = models.ForeignKey(CustomUser)
    # def __unicode__(self):
    # return self.title

