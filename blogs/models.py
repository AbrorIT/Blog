from tabnanny import verbose
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщения"
        verbose_name_plural = "Сообщении"