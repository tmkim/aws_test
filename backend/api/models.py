from django.db import models

# Create your models here.
class Image(models.Model):
    image_variable = models.ImageField(null=True, default="{default_filename)", upload_to='uploads/') 
