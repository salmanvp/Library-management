from django.db import models

class book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.IntegerField(null=True)
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/image',null=True,blank=True)
    def __str__(self):
        return self.title


class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    def __str__(self):
        return self.name

