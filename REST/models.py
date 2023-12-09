from distutils.command.upload import upload
from django.db import models

class Image(models.Model):

    caption=models.TextField()
    image=models.ImageField(upload_to="images/")
    

    def __str__(self):
        return self.caption
