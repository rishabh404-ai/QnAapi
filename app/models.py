from django.db import models

# Create your models here.
class Questions(models.Model):
    Text = models.TextField(max_length=None)
    Image = models.ImageField(upload_to='media')
    Tags = models.CharField(max_length=100)
   
    def __str__(self):
        return self.Text
     