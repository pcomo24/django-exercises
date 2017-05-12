from django.template.response import TemplateResponse
from django import http
import datetime
from django.core.mail import send_mail
from django import forms
import forms

def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})

def american (request):
  return TemplateResponse(request, 'american.html', {})

def thanks (request):
  return TemplateResponse(request, 'thanks.html', {})

def hello (request):
  form  = NameForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      print(form.cleaned_data['your_name'])
      return http.HttpResponseRedirect('/american/')

  return TemplateResponse(request, 'hello.html', {})



def contact_me (request):
    form = forms.QuestionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            the_name = form.cleaned_data['your_name']
            the_message = form.cleaned_data['your_message']
            the_email = 'paul@paulrcomo.com'
            send_mail(the_name, the_message, the_email,['pcomo24@gmail.com'],fail_silently=False)
            return http.HttpResponseRedirect('/thanks/')
    return TemplateResponse(request, 'contact_me.html', {})
