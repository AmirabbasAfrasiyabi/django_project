from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey('users.User' ,  on_delete=models.CASCADE , related_name='articles')
    creat_at = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey('Category' , on_delete=models.PROTECT , related_name='articles')

class Category(models.Model):
    title= models.CharField(max_length=50) 