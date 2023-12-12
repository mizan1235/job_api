from django.db import models

# Create your models here.
class user_cred(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    username=models.CharField(max_length=40,primary_key=True)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
class employee_cred(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    username=models.CharField(max_length=40,primary_key=True)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
class job_details(models.Model):
    company_logo=models.ImageField(upload_to='media/',max_length=250,null=True,default=None)
    company_name=models.CharField(max_length=100)
    company_title=models.CharField(max_length=200)
    location=models.CharField(max_length=50)
    date=models.CharField(max_length=40)
    job_id=models.CharField(max_length=70)
    apply_link=models.CharField(max_length=400,default="#")
    username=models.CharField(max_length=40,default='rahul123')

