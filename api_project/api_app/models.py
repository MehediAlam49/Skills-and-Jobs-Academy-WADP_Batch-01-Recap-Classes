from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)
    department=models.CharField(max_length=100, null=True)


    def __str__(self):
        return f'{self.name}'
