from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField(upload_to="blog-images/")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)  
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.author} at {self.post}"
    