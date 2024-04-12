from django.db import models

# Create your models here.
class Election(models.Model):
    election = models.CharField(max_length = 255)
    is_over = models.BooleanField(default=False)
    description = models.TextField(default='A POLL')
    winner = models.CharField(max_length = 255, null = True)

    def __str__(self):
        return f"{self.election}"
    
class vote(models.Model):
    voter = models.IntegerField()
    candidate = models.CharField(max_length = 255)
    election = models.ForeignKey(to=Election, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voter} {self.candidate} {self.election}"
    
    