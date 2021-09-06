from django.db import models
from django.db.models.expressions import Value

# Create your models here.
class student(models.Model):
    name =models.CharField(max_length=200)
    roll_number= models.CharField(max_length=10)
    date_of_birth = models.DateTimeField()
    marks = models.IntegerField()

    def dist(self):
        x = student.objects.filter(marks__range=(91, 100)).count()
        z = student.objects.filter(marks__range=(0, 100)).count()
        y = (x/z)*100
        return y

    def first(self):
        x = student.objects.filter(marks__range=(81, 91)).count()
        z = student.objects.filter(marks__range=(71, 81)).count()
        s = student.objects.filter(marks__range=(0, 100)).count()
        y = ((x+z)/s)*100
        return y
    def pas(self):
        z = student.objects.filter(marks__range=(55, 100)).count()
        s = student.objects.filter(marks__range=(0, 100)).count()
        y = (z/s)*100
        return y
    

    def __str__(self):
        return self.name