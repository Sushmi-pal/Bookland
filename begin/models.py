from django.db import models

class Contact(models.Model):
    sn=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    phone=models.CharField(max_length=20)
    content=models.TextField()


    def __str__(self):
        return self.name


