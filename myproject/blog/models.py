from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lnglat = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[-1].strip()
        return None
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0].strip()
        return None
class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
