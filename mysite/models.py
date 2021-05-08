from django.db import models

class Person(models.Model):
    email = models.EmailField(max_length=45, unique=False, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Orders(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    
    