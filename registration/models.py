from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sex(models.Model):
   sex = models.TextField('Пол пользователя', max_length=100)
   
   def __str__(self) -> str:
       return "Пол:"
   
   
   class Meta:
      verbose_name = "Пол"
      verbose_name_plural = "Пол"
   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='avatar.png', upload_to='user_images')
    
    def __str__(self) -> str:
        return f'Профаил пользователя {self.user.username}'
    
    class Meta:
        verbose_name = 'Профаил'
        verbose_name_plural = 'Профаилы'
        