from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length= 50 , unique=True)
    
    description = models.TextField(null = True , blank=True)
    # User = models.ForeignKey(User, on_delete=models.CASCADE)

   

    def __str__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING' , 'PENDING'),
        ('IN PROGRESS' , 'IN PROGRESS'),
        ('COMPLETED' , 'COMPLETED'),
    ]
    
    title=models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 12 , choices = STATUS_CHOICES , default = 'PENDING')
    priority = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(3)] ,null= True , blank= True) 
    due_date = models.DateField(null= True , blank=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    category= models.ForeignKey(Category ,on_delete=models.CASCADE)
    def __str__(self):
        return self.title




 
class comment(models.Model):
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)


    task = models.ForeignKey(Task , on_delete = models.CASCADE)