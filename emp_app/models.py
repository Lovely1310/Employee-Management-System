from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100 , null = False)
    def __str__(self):
        return self.name

# Create your models here.
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    phone_number = models.CharField(max_length=10, default='0000000000')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default='Unknown')
    hire_date = models.DateField()  

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"



