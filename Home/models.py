from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=15)
    massage=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return 'Massage From ' + self.name +' - ' +self.email
    

