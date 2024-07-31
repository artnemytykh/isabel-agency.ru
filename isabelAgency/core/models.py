from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=16)
    email = models.CharField(max_length=128)
    website = models.CharField(max_length=1024, null=True, blank=True)
    company = models.CharField(max_length=128)
    role = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.pk}: {self.company}"