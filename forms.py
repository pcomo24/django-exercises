from django import forms

class NameForm (forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class QuestionForm (forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    your_email = forms.EmailField(label='Your Email', max_length=100)
    your_message = forms.CharField(label='Your Message', max_length=1000)
