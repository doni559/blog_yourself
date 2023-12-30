from .models import Articles
from django.forms import ModelForm,TextInput, Textarea, DateInput

class ArticlesForm(ModelForm):
    class Meta():
        model = Articles
        fields=['title', 'anounce', 'full_text', 'date', 'user']
        widgets={
            "title": TextInput(attrs={
                "placeholder" : 'Название',
                "class": "form-control"
            }),
            "anounce": TextInput(attrs={
                "placeholder" : 'Анонс',
                "class": "form-control"
            }),
            "full_text": Textarea(attrs={
                "placeholder" : 'Название',
                "class": "form-control"
            }),
            "date": DateInput(attrs={
                "class": "form-control",
                "placeholder":"Дата публикации"
            }),
            "user": TextInput(attrs={
                "class": "form-control",
                "placeholder":"Пользователь",
                "type": "hidden",
                

            })
        }
class EditArticlesForm(ModelForm):
    class Meta():
        model = Articles
        fields=['title', 'anounce', 'full_text']
        widgets={
            "title": TextInput(attrs={
                "placeholder" : 'Название',
                "class": "form-control"
            }),
            "anounce": TextInput(attrs={
                "placeholder" : 'Анонс',
                "class": "form-control"
            }),
            "full_text": Textarea(attrs={
                "placeholder" : 'Название',
                "class": "form-control"
            }),
            "date": DateInput(attrs={
                "class": "form-control",
                "placeholder":"Дата публикации"
            }),
            "user": TextInput(attrs={
                "class": "form-control",
                "placeholder":"Пользователь",
                "type": "hidden",
                

            })
        }