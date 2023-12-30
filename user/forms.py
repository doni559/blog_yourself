from django import forms
from .models import AllUsersData
from django.forms import ModelForm,TextInput, Textarea, DateInput


class LoginForm(forms.Form):
    nickname = forms.CharField(label='Никнейм', max_length=25, min_length=3, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль", min_length=5, required=True)

class EditProfile(ModelForm):
    class Meta():
        model = AllUsersData
        fields=['about', 'status']
        widgets={
            "about": TextInput(attrs={
                "placeholder" : 'Напишите немного о себе',
                "class": "form-control"
            }),
            "status": TextInput(attrs={
                "placeholder" : 'Введите статус',
                "class": "form-control"
            })
        }
