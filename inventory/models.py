from django.db import models

# Create your models here.
class Autor(models.Model):
    name = models.CharField(max_length=200)
    funado = models.BooleanField()

    def __str__(self):
        return self.name

class Libro(models.Model):
    title = models.CharField(max_length=200)
    stock = models.IntegerField()
    last_update = models.DateTimeField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)