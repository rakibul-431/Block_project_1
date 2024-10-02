from django.db import models
from categories.models import categories
from author.models import author

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(categories)
    author=models.ForeignKey(author,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
