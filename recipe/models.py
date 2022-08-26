from django.db import models
from category.models import Category
# Create your models here.






class Recipe(models.Model):
    title=models.CharField(max_length=100)
    ingredients=models.TextField()
    recipe=models.TextField()
    
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    image=models.ImageField(upload_to='images', null=True, blank=True)



    class Meta:
        ordering=['title']

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    owner=models.ForeignKey('account.CustomUser',
    related_name='comments', on_delete=models.CASCADE)
    post=models.ForeignKey(Recipe, related_name='comments',on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.owner} -> {self.created_at}'


class Likes(models.Model):
    post=models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='likes')
    owner=models.ForeignKey('account.CustomUser',on_delete=models.CASCADE,related_name='liked')

    class Meta:
        unique_together=['post','owner']
