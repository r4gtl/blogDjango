from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

FIXING_STATUS = (
    (0, "Not fixed"),
    (1, "Fixed Left"),
    (2, "Fixed Right")
)

class PostCategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return(self.name)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    fixing_status = models.IntegerField(choices=FIXING_STATUS, default=0)
    logo_post = models.ImageField(blank=True, null=True)    
    category = models.ForeignKey(PostCategory, on_delete=models.DO_NOTHING, related_name='category', default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'. format(self.body, self.name)


