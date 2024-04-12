from django.db import models
from voting.models import Election

# Create your models here.
class Candidate(models.Model):
    username = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255, default='Ganesh')
    Election = models.ForeignKey(Election, on_delete=models.CASCADE)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.username} {self.Election}"

# class Voters(models.Model):
#     name = models.CharField(max_length = 255)
#     email = models.EmailField()