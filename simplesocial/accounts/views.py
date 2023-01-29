from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from.import form
# Create your views here.


class SignUp(CreateView):
    form_class = form.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
