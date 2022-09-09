from django.db import models
from category.models import Category
# Create your models here.



from django.contrib.auth import get_user_model


User=get_user_model()


class Post(models.Model):
    title=models.CharField(max_length=100)
    
    post=models.TextField()
    
    tag=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image=models.ImageField(upload_to='images', null=True, blank=True)



    class Meta:
        ordering=['title']

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post=models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} -> {self.created_at}'


class Likes(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='likes')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked')

    class Meta:
        unique_together=['post','user']


class Favorites(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['post', 'user']
