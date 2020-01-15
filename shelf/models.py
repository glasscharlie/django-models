from django.db import models

class Shelf(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    img = models.TextField()

    def __str__(self):
        return self.title