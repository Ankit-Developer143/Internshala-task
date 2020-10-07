from django.db import models
from datetime import datetime,date
# Create your models here.





class Data(models.Model):
     CATEGORY = (
         ('Corporate Headoffice','Corporate Headoffice'),
        
         ('Operations Department','Operations Department'),
         ('Work Station','Work Station'),
         ('Marketing Division','Marketing Division')
     )
     initial = (
         ('Mild','Mild'),
         ('Moderate','Moderate'),
         ('Severe','Severe'),
         ('Fatal','Fatal'),
        
     )
     
     Location = models.CharField(max_length=200, null=True, choices=CATEGORY)
     incident_location = models.TextField(max_length=200)
     initial_Severity =models.CharField(max_length=200, null=True, choices=initial)
     Immedate_Action_Taken =  models.TextField(max_length=200)
     Reported_By = models.CharField(max_length=200)
    
    

    
    