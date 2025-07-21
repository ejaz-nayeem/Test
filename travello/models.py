from django.db import models

# Create your models here.
class Destination(models.Model):
    
    destination_name=models.CharField(max_length=100)
    
    description=models.TextField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)

# class Destination2:
#     id:int
#     destination_name:str
    
#     description:str
#     price:int
#     image:str
    
# class Destination3:
#     id:int
#     destination_name:str
    
#     description:str
#     price:int
#     image:str
        