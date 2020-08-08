from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heah0 = models.CharField(max_length=500)
    cheah0 = models.CharField(max_length=5000)
    heah1 = models.CharField(max_length=500)
    cheah1 = models.CharField(max_length=5000)
    heah2 = models.CharField(max_length=500)
    cheah2 = models.CharField(max_length=5000)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.title
    
