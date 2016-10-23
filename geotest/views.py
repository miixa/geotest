# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render_to_response, HttpResponseRedirect
from geotest import forms  # AddClientForm, EditClientForm, AddOrganizationForm, EditOrganizationForm, AddCarForm
from geotest import models
from django.template import RequestContext
# from models import Clients, Organization, Car
# import string, random
# from django.contrib.auth.forms import User
# from django.contrib import auth
# import os
# from models import file_path

def subject_view(request):
    csrfContext = RequestContext(request)
    args = {
        'subject': models.Subject.objects.filter(user_id=0),
        'addSubjectForm': forms.addSubjectForm,
    }
    return render_to_response('subjecttempl.html',args,csrfContext)

def addSubject_view(request):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addSubjectForm(request.POST or None)
        if form.is_valid():
            subject = {
                'title':  form.cleaned_data['subject'],
                'user_id': 0
            }
            model_subject = models.Subject(**subject)
            model_subject.save()
    return HttpResponseRedirect('/test/subject', csrfContext)

def theme_view(request,subject_id):
    csrfContext = RequestContext(request)
    args = {
        'subject_id': subject_id,
        'theme': models.Theme.objects.filter(user_id=0,subject_id=subject_id),
        'addThemeForm': forms.addThemeForm,
    }
    return render_to_response('themetempl.html',args,csrfContext)

def addTheme_view(request,subject_id):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addThemeForm(request.POST or None)
        if form.is_valid():
            theme = {
                'title':  form.cleaned_data['theme'],
                'subject_id': subject_id,
                'user_id': 0,
            }
            model_theme = models.Theme(**theme)
            model_theme.save()
    return HttpResponseRedirect('/test/theme/'+subject_id)

def question_view(request,subject_id,theme_id):
    csrfContext = RequestContext(request)
    args = {
        'subject_id': subject_id,
        'theme_id': theme_id,
        'question': models.Question.objects.filter(user_id=0,subject_id=subject_id,theme_id=theme_id),
        'addQuestionForm': forms.addQuestionForm,
    }
    return render_to_response('questiontempl.html',args,csrfContext)

def addQuestion_view(request, subject_id, theme_id):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addQuestionForm(request.POST or None)
        if form.is_valid():
            question = {
                'title':  form.cleaned_data['question'],
                'subject_id': subject_id,
                'theme_id': theme_id,
                'user_id': 0,
            }
            model_question = models.Question(**question)
            model_question.save()
    return HttpResponseRedirect('/test/question/'+subject_id+'/'+theme_id)

def answer_view(request,subject_id,theme_id, question_id):
    csrfContext = RequestContext(request)
    args = {
        'subject_id': subject_id,
        'theme_id': theme_id,
        'question_id': question_id,
        'question': models.Question.objects.filter(user_id=0, subject_id=subject_id,
                                                   theme_id=theme_id,id=question_id),
        'answer_correct': models.CorrectAnswer.objects.filter(user_id=0,subject_id=subject_id,
                                                              theme_id=theme_id,question_id=question_id),
        'answer_incorrect': models.IncorrectAnswer.objects.filter(user_id=0, subject_id=subject_id,
                                                                  theme_id=theme_id,question_id=question_id),
        'addAnswerCorrectForm': forms.addAnswerCorrectForm,
        'addAnswerInCorrectForm': forms.addAnswerInCorrectForm,

    }
    return render_to_response('answertempl.html',args,csrfContext)

def addAnswerCorrect_view(request, subject_id, theme_id, question_id):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addAnswerCorrectForm(request.POST or None)
        if form.is_valid():
            answer_correct = {
                'title':  form.cleaned_data['answer_correct'],
                'subject_id': subject_id,
                'theme_id': theme_id,
                'question_id': question_id,
                'user_id': 0,
            }
            model_answer = models.CorrectAnswer(**answer_correct)
            model_answer.save()
    return HttpResponseRedirect('/test/answer/' + subject_id + '/' + theme_id + '/' + question_id)

def addAnswerInCorrect_view(request, subject_id, theme_id, question_id):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addAnswerInCorrectForm(request.POST or None)
        if form.is_valid():
            answer_incorrect = {
                'title':  form.cleaned_data['answer_incorrect'],
                'subject_id': subject_id,
                'theme_id': theme_id,
                'question_id': question_id,
                'user_id': 0,
            }
            model_answer = models.IncorrectAnswer(**answer_incorrect)
            model_answer.save()
    return HttpResponseRedirect('/test/answer/'+subject_id+'/'+theme_id+'/'+question_id)
#def addSubject_view(request):
#    csrfContext = RequestContext(request)
#    if request.method == 'POST':
#        form = forms.addQuestionForm(request.POST or None)
#        if form.is_valid():
#            subject = {
#                'title':  form.cleaned_data['subject'],
#                'user_id': 0
#            }
#            model_subject = models.Subject(**subject)
#            model_subject.save()
#            return render_to_response('subjecttempl.html', args, csrfContext)
#    args = {'subject': forms.addQuestionForm}
#    return render_to_response('subjecttempl.html', args, csrfContext)

#def addQuestion(request):
#    """
#
#    :type request: object
#    """
#    csrfContext = RequestContext(request)
#    if request.method == 'POST':
#        form = forms.addQuestionForm(request.POST or None)
#        if form.is_valid():
#            subject = {
#                'title':  form.cleaned_data['subject'],
#                'user_id': 0
#            }
#            theme = {
#                'title': form.cleaned_data['theme'],
#                'subject_id': form.cleaned_data['subject'],
#            }
#            model_subject = models.Subject(**subject)
#            model_subject.save()
#            model_theme = models.Theme(**theme)
#            model_theme.save()
#            return render_to_response('addquestion.html', args, csrfContext)
#    args = {'addQuestion': forms.addQuestionForm}
#    return render_to_response('addquestion.html', args, csrfContext)

# def AddClient (request):
#    """
#
#    :type request: object
#    """
#    print(request)
#    if request.method == 'POST':
#        form = AddClientForm(request.POST)
#        if form.is_valid():
#            def rand_passw():
#                rid = ''
#                for x in range(8): rid += random.choice(string.ascii_letters + string.digits)
#                return rid
#            def rand_id():
#                rid = ''
#                for x in range(8): rid += random.choice(string.digits)
#                return rid
#            django_user_args = {}
#            django_user_args['username'] = "id" + rand_id()
#            django_user_args['password'] = rand_passw()
#            django_user = User(**django_user_args)
#            django_user.save()
#            args = {}
#            args["SimvolName"] = form.cleaned_data["SimvolName"]
#            args['pin'] = User.objects.get(username = django_user_args['username'])
#            model_client = Clients(**args)
#            model_client.save()
#            return HttpResponseRedirect('/operator/tableclient')
#    args = {}
#    args['username'] = auth.get_user(request).username
#    args['form_client'] = AddClientForm
#    return render_to_response('add_client.html',args,RequestContext(request))
