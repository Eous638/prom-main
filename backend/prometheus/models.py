from django.db import models

class Product(models.Model):
    title = models.CharField(max_length= 70)
    description = models.TextField()
    price = models.FloatField()
    image = models.FileField(upload_to='static/images')
    id_field = models.AutoField(primary_key=True)
    category = models.ManyToManyField('Category', related_name='product')
    
    def __str__(self):
        return self.title
    

    
class SuperCategory(models.Model):
    title = models.CharField(max_length= 70)
    image = models.FileField(upload_to='static/images')
    id_field = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Super Categories"

class Category(models.Model):
    image = models.FileField(upload_to='static/images')
    title = models.CharField(max_length= 70)
    id_field = models.AutoField(primary_key=True)
    supercategory = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, related_name='category')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"