from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
class Blogpost(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        published = models.DateTimeField(auto_now_add=True)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        def __str__(self):
            return self.title