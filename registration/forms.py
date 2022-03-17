from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Sex

class UserRegisterForm(UserCreationForm):
   email=forms.EmailField(
      label='Введите e-mail',
      required=True,
      widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите e-mail тут'})
      )
   username = forms.CharField(
      label='Введите логин',
      required=True, 
      help_text='Нельзя вводить символы: @, /, _',
      widget=forms.TextInput(attrs={'class':'form-control'})
      )
   #choose_sex = forms.ModelChoiceField(queryset=Sex.objects.all(),label='Выберите пол')
   password1 = forms.CharField(
      label='Введите пароль',
      required=True, 
      help_text='Пароль не должен быть простым',
      widget=forms.PasswordInput(attrs={'class':'form-control'})
      )
   password2 = forms.CharField(
      label='Подтвердите пароль',
      required=True,       
      widget=forms.PasswordInput(attrs={'class':'form-control'})
      )
   
  
   
   
   class Meta:
      model = User
      fields = ['email', 'username', 'password1','password2']