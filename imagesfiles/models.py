from django.db import models

class images(models.Model):
    id_no=models.IntegerField()
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    profile=models.FileField(upload_to='files')

    def __str__(self):
        return self.name