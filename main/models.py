from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Description(models.Model):
    book_name=models.CharField(max_length=100)
    edition=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    price=models.CharField(max_length=50)
    book_image=models.ImageField(upload_to='book_pic')
    phone=models.CharField(max_length=20,default='')
    seller=models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('main:detail',kwargs={'pk':self.pk})