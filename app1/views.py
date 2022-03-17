from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home (request):
   number = 50
   news =[
      {
         'title': 'first article',
         'text': 'full text',
         'date': ' 1/01/2021',
         'avtor': 'Serg'
         
      },
      {
         'title': 'second article',
         'text': 'full text second art',
         'date': ' 2/01/2021',
         'avtor': 'Lera'
         
      }
   ]
   data = {
      'news': news,
      'title': 'Главная страница'
   }
   
   
   
   return render(request, 'app1/home.html', data)

def contacti (request):
   
   
   contacti = {
      'title': 'Контакты',
   }
   
   return render(request, 'app1/contacti.html', contacti)


