from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class team(models.Model):
    name_team = models.CharField(max_length=250)
    img_team = models.ImageField(upload_to='pics1')
    desc_team = models.TextField()
    #def __str__(self):
     #   return self.name()
