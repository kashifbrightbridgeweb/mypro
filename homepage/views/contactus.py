from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from homepage import models
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django import forms



class PracticeBCForm(forms.Form):
  fromEmail = forms.EmailField(max_length=300, required=True, widget=forms.TextInput({ "placeholder": "Enter Your email"}), label=False)
  Subject = forms.CharField(max_length=30, required=True, widget=forms.TextInput({ "placeholder": "Subject "}), label=False)
  Message = forms.CharField(max_length=3000, required=True, widget=forms.Textarea({ "placeholder": "Enter Message here"}), label=False)

@view_function
def send_email(request):
    from_email = request.POST.get('fromEmail', '')
    subject = request.POST.get('Subject', '')
    message = request.POST.get('Message', '')
    if subject and message and from_email:
        try:
            send_mail(subject,
             message, from_email,
               ['seramomollc@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contactus')
    else:
        return HttpResponseRedirect('/contactus/error')




@view_function
def process_request(request):
  form = PracticeBCForm()
  context = {
    'now': datetime.now(),
    'request': request,
    'form': form,
  }
  return dmp_render(request, 'contactus.html', context)

