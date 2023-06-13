from django.db import models

# Create your models here.
class product_catagory(models.Model):
    catagory_name=models.CharField(max_length=100)
    catagory_id=models.PositiveIntegerField()
    def __str__(self):
        return self.catagory_name
    



class Product(models.Model):
    category_name=models.ForeignKey(product_catagory, on_delete=models.CASCADE)
    Pname=models.CharField(max_length=100)
    Pid=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.Pname

        
    
    
    
    



