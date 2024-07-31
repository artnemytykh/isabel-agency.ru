from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Post #{self.pk}: {self.title}. {self.date}"