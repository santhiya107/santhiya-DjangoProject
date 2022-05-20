from a_app.models import log
from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    user= models.ForeignKey(log,on_delete=models.SET_NULL,null =True)
   
    created=models.DateTimeField(auto_now_add=True)
    due_time=models.IntegerField(default=0,blank=True)
    consumed_hours=models.IntegerField(default=0,blank=True)
    remaining_hours=models.IntegerField(default=0,blank=True)
    completed=models.BooleanField(default=False)
  
    
    def __str__(self):
        return self.title
