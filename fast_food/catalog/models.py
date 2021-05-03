from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=30)
    parent =  models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    sort_order=models.IntegerField()

    def __str__(self):
        return self.name


class Product_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product_image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_main = models.BooleanField()
