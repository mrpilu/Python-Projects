from django.db import models

# Create your models here.

class UniversityClasses(models.Model):
    title = models.CharField(max_length=200)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=200)
    duration = models.FloatField()

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "University Classes"

    def __str__(self):
        return f"{self.title}: {self.instructor_name}"
