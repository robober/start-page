# -*- coding:utf-8 -*-

from django.forms import Field, ModelForm, PasswordInput
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(ModelForm):
    username = forms.CharField(label='Логин', error_messages={'required': 'Укажите логин'})
    password = forms.CharField(label='Пароль', widget=PasswordInput(),
                               error_messages={'required': 'Укажите пароль'})
    password_again = forms.CharField(label='Повторите пароль', widget=PasswordInput(),
                                     error_messages={'required': 'Укажите пароль еще раз'})

    class Meta:
        model = User
        fields = ['username', 'password']
        # exclude = ('user', 'password', 'password_again')

    # Валидация проходит в этом методе
    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Пароли должны совпадать!')
        return self.cleaned_data