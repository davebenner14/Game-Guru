from django.db import models
from django.urls import reverse
from datetime import date

PROGRESS = (
    ('S', 'Started'),
    ('I', 'In-progress'),
    ('C', 'Completed')
)
# Create your models here.

class Character(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

class Vid(models.Model):
    name = models.CharField(max_length=100)
    console = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release = models.IntegerField()
    characters = models.ManyToManyField(Character)

    #  new code below
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'vid_id': self.id})

class Progress(models.Model):
    date = models.DateField('Progress date')
    progress = models.CharField(
        max_length=1,
        choices=PROGRESS,
        default=PROGRESS[0][0]
    )
    vid = models.ForeignKey(Vid, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_progress_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']