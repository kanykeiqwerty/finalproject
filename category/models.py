from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    slug=models.SlugField(max_length=30, primary_key=True)
    name=models.CharField(max_length=30, unique=True)
    parent=models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='category',
        blank=True,
        null=True
    )
    
    def __str__(self) -> str:
        return f'{self.name} --> {self.parent}' if self.parent else self.name


    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name} --> {self.parent}' if self.parent else self.name
