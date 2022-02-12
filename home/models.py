from django.db import models

class Test_simulation (models.Model):
    title_simulation  = models.CharField(max_length=50)
    tags_simulation  = models.CharField(max_length=20)
    rate_simulation  = models.IntegerField()

    def __str__(self):
        return self.title_simulation
