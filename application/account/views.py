from .models import User 
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView, CreateView
from django.views.generic import TemplateView
from .forms import LoginForm, CreateUserForm
from django.contrib import auth
from django.http import HttpResponseRedirect


class LoginView(FormView):

    form_class = LoginForm
    success_url = '/'
    template_name = 'account/login.html'

    def get_form_kwargs(self):
        form_kwargs = super(LoginView, self).get_form_kwargs()
        form_kwargs.update({
            'request': self.request
        })
        return form_kwargs

    def form_valid(self, form):
        return redirect(self.get_success_url())

class UserProfileView():
    pass


class CreateUserView(CreateView):
    """
    Create new user
    """
    form_class = CreateUserForm
    model = User
    success_url = '/'
    template_name = 'account/create_user.html'

    def form_valid(self, form):
        super(CreateUserView, self).form_valid(form)
        return redirect(self.get_success_url())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('account:login'))
