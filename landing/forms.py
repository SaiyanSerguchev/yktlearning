from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'readonly class': 'form-control-plaintext'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'readonly class': 'form-control-plaintext'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'readonly class': 'form-control-plaintext'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfileForm(ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(label='Новый пароль', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(label='Подтвердите новый пароль', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')