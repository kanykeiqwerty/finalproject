from django.db import models
from recipe.models import Post
from django.contrib.auth import get_user_model


User=get_user_model()

class Mark():
    one=1
    two=2
    three=3
    four=4
    five=5
    marks=(
        (one, 'too bad'), 
        (two, 'bad'),
        (three, 'normal'),
        (four, 'good'), 
        (five, 'excellent'),
    )

class Review(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')

    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    text=models.TextField()
    rating=models.IntegerField(choices=Mark.marks)
    created_at=models.DateTimeField(auto_now_add=True)
    

