from django.db import models


class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=200)

    def __str__(self):
        return self.coursename


class details(models.Model):
    couse = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    SP = models.CharField(max_length=500)
    il = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)
