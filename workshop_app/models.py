from django.db import models

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    trainer = models.CharField(max_length=100) 
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    target_audience = models.CharField(max_length=200) 

    def __str__(self):
        return self.title