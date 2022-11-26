from django.db import models

class place(models.Model):
   name=models.CharField(max_length=200)
   img=models.ImageField(upload_to='picture')
   desc=models.TextField()
   price=models.IntegerField()
   offer=models.BooleanField(default=False)