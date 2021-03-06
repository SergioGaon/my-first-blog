from django.db import models
from django.utils import timezone
from django.db import connections



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cliente(models.Model):
    
	cl_cod=models.IntegerField()
	cl_nom=models.CharField(max_length=100)
	cl_edad=models.IntegerField()
	cl_dir=models.CharField(max_length=100)
	cl_tel=models.CharField(max_length=100)
	cl_email=models.CharField(max_length=100)
