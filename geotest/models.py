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

class CorrectAnswer(models.Model):
    title = models.CharField(max_length=400)
    question = models.ForeignKey(Question)
    subject = models.ForeignKey(Subject)
    theme = models.ForeignKey(Theme)
    user = models.ForeignKey(CustomUser)
    Uid_id = models.IntegerField(max_length=10,null=True)
    # def __unicode__(self):
    # return self.title

class IncorrectAnswer(models.Model):
    title = models.CharField(max_length=400)
    question = models.ForeignKey(Question)
    subject = models.ForeignKey(Subject)
    theme = models.ForeignKey(Theme)
    user = models.ForeignKey(CustomUser)
    Uid_id = models.IntegerField(max_length=10, null=True)
    # def __unicode__(self):
    # return self.title

class Uid (models.Model):
    CorrectAnswer_id = models.IntegerField(max_length=10,null=True)
    IncorrectAnswer_id = models.IntegerField(max_length=10, null=True)