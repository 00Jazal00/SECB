from django.db import models

# Create your models here.
class NEWSLETTER(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, default="")
    def __str__(self):                                  
        return self.email
