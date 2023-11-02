from django.db import models

# Create your models here.
# file model to upload file
class File(models.Model):
    file= models.FileField(upload_to="files")

# Company model 
class Company(models.Model):
    name= models.CharField(max_length=150)
    domain= models.CharField(max_length=150,null=True)
    year_founded=models.CharField(max_length=4,null=True)
    industry=models.CharField(max_length=150,null=True)
    size_range=models.CharField(max_length=100,null=True)
    locality=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    linkedin_url=models.CharField(max_length=200,null=True)
    current_employee_estimate=models.IntegerField(null=True)
    total_employee_estimate=models.IntegerField(null=True)
