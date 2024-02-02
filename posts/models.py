from django.db import models

# Create your models here.
class File ( models.Model):
    file = models.FileField(upload_to="file")

    
    
class Posts(models.Model):
    name= models.CharField(max_length = 40)
    example= models.CharField(max_length = 50)
    description= models.CharField(max_length = 50)
    
    def __str__(self) :
        return self.name