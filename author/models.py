from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    mobile = models.CharField(max_length=12)

    def __str__(self) -> str:
        return f"Name : {self.name} Mobile : {self.mobile}"

