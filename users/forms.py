from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'r_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'r_sname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'r_uname'}))
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={'id': 'r_tel'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'r_mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'r_pass'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'r_passp'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'inp_reg'

class UserProfile(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, 'id': 'r_izm_uname'}))
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={'readonly': True, 'id': 'r_izm_tel'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True, 'id': 'r_izm_mail'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'r_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'r_sname'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone', 'email')

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'inp_reg'