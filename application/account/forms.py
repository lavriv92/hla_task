from django import forms
from models import User
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    """
    Form for login
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs = {
            'placeholder': _('username')
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder': _('password')
        }
    ))

    def __init__(self, request, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError(_('User is not authenticated'))
        auth.login(self.request, user)
        return cleaned_data
        

class CreateUserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs = {
            'placeholder': _('username')
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'role']
    
    def __init__(self, *args, **kwargs):
        self.base_fields['username'].help_text = None
        for key in self.base_fields:
            self.base_fields[key].label = ''
            self.base_fields[key].placeholder = key
        super(CreateUserForm, self).__init__(*args, **kwargs)

