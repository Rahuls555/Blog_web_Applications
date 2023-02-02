
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=250)
    # content=models.TextField()
    content=RichTextField()
    author=models.CharField(max_length=250)
    slug=models.CharField(max_length=150)
    timestamp = models.DateTimeField(blank=True,null=True,default=now)
    
    def __str__(self):
        return self.title +' by - ' + self.author
    
class blogcomment(models.Model):
  
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)

    
    
    
