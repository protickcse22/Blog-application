from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title   = models.CharField(max_length=100) 
    slug    = models.SlugField(default='')
    body    = models.TextField(blank=False) 
    date    = models.DateTimeField(auto_now_add=True)
    thumb   = models.ImageField(default='dafalut.png',blank=True)
    author    = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + "..."