# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import RegistrationForm


def registrate(request):
    if request.method == 'POST':

        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            """user = User(username=form.cleaned_data['login'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            """
            try:
                form.save()
            except Exception:
                error = "Некорректное имя пользователя!"
                return render(request, 'registrate.html', {'form': form, 'error': error})

            # print(form.user, form.password, form.password_agaihn)
            # print form.cleaned_data
            return HttpResponse('Форма верна!')
    else:
        form = RegistrationForm()
    return render(request, 'registrate.html', {'form': form})
