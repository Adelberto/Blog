from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = models.TextField()
  #TO DO - change DateTimeField format - waiting for stackoverflow answer!
  date = models.DateTimeField(auto_now_add=True)
  thumb = models.ImageField(default="default.jpeg",blank=True)
  author = models.ForeignKey(User, default=None,on_delete=models.SET_DEFAULT)

  def __str__(self):
    return self.title

  
  def snippet(self):
    return self.body[:30]+ '...'