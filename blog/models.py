from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images')
    urls = models.URLField(blank=True)

    def __str__(self):
        return self.title
