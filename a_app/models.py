
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


# Create your models here.
class manager(BaseUserManager):
    use_in_migrations = True
    def normalize_email(self,name):
        return name.strip().lower()
    
    
    
    
    def __create(self,email,username,password):
        if not email and not password and not username:
            raise ValueError("you should have a email")
        user=self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create(self,email,username,password=None):
        user=self.__create(email,username,password)
        user.save()
        return user
    
    def create_superuser(self,email,username,password):
        user = self.__create(email,username,password)
        user.is_admin = True
     
        user.save()
        return user

    
        
class log(AbstractBaseUser):    
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=20)    
    created_date=models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
 
  

    is_admin = models.BooleanField(default=False)
   
    

    objects=manager()
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
    
    
    def has_perm(self , obj=None):
        return True

    def has_module_perms(self , app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    
class Profile(models.Model):
        
    user = models.OneToOneField(log,on_delete=models.CASCADE,null =True)
    full_name = models.CharField(max_length=255)    
    contact = models.IntegerField()
    country = models.CharField(max_length=50)
    profession=models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='images',null=True,blank=True)
 
    
    def __str__(self):
        return str(self.user)