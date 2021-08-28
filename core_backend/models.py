from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

 
#Our First Database Model
class Post(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default='')
    suite = models.CharField(max_length=200, default="")
    account_number = models.CharField(max_length=200, default='')
    photo = models.URLField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    courier = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
        
        

        





#Our Second Database Model
class About_Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)  
    
    def __str__(self):
        return self.title


    
