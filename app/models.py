from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name= models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'


class Subscription(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.email}'
