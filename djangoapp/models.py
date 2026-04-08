from django.db import models

# Create your models here.

class Category(models.Model):
    Category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Category
    
class DressInfo(models.Model):
    dress_name = models.CharField(max_length=200)
    dress_price = models.CharField(max_length=50)
    dress_image = models.URLField(max_length=6000)
    dress_category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dress_name
    
