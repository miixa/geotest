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
        'subject': models.Subject.objects.filter(user_id=0)
    }
    return render_to_response('subjecttempl.html',args,csrfContext)

def addSubject_view(request):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addQuestionForm(request.POST or None)
        if form.is_valid():
            subject = {
                'title':  form.cleaned_data['subject'],
                'user_id': 0
            }
            model_subject = models.Subject(**subject)
            model_subject.save()
            return render_to_response('subjecttempl.html', args, csrfContext)
    args = {'subject': forms.addQuestionForm}
    return render_to_response('subjecttempl.html', args, csrfContext)

def addQuestion(request):
    """

    :type request: object
    """
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = forms.addQuestionForm(request.POST or None)
        if form.is_valid():
            subject = {
                'title':  form.cleaned_data['subject'],
                'user_id': 0
            }
            theme = {
                'title': form.cleaned_data['theme'],
                'subject_id': form.cleaned_data['subject'],
            }
            model_subject = models.Subject(**subject)
            model_subject.save()
            model_theme = models.Theme(**theme)
            model_theme.save()
            return render_to_response('addquestion.html', args, csrfContext)
    args = {'addQuestion': forms.addQuestionForm}
    return render_to_response('addquestion.html', args, csrfContext)

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
