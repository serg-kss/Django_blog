from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.contrib.auth.models import User

# Create your models here.

class Articles (models.Model):
   title = models.CharField("Название статьи", max_length=100)
   text = models.TextField("Текст статьи", default="some text")
   date = models.DateField("Дата", auto_now=False, auto_now_add=False)
   avtor = models.ForeignKey(User, verbose_name="Автор", on_delete=CASCADE)
   
   def __str__(self) -> str:
       return f'Статья: {self.title}'
    
    
    
   class Meta:
      verbose_name = "Статья"
      verbose_name_plural = "Статьи"
   
