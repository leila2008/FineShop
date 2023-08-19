from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Никнейм', required = True , widget = forms.TextInput(attrs={'class': 'lf--input', 'placeholder': 'Никнейм'}))
    first_name = forms.CharField(label = 'Имя', required = True , widget = forms.TextInput(attrs={'class': 'lf--input' , 'placeholder': 'имя'}))
    last_name = forms.CharField(label = 'Фамилия', required = True , widget = forms.TextInput(attrs={'class': 'lf--input', 'placeholder': 'фамилия'}))
    password1 = forms.CharField(label = 'Пароль', required = True , widget = forms.PasswordInput(attrs={'class': 'lf--input', 'placeholder': 'пароль'}))
    password2 = forms.CharField(label = 'Повторите пароль', required = True , widget = forms.PasswordInput(attrs={'class': 'lf--input', 'placeholder': 'повторите пароль'}))
    email = forms.EmailField(label = 'E-mail', required = True , widget = forms.TextInput(attrs={'class': 'lf--input', 'placeholder': 'E-Mail'}))

    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'password1' , 'password2' , 'email')
    def save(self,commit = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user