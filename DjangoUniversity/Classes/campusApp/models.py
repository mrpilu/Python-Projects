
# Import Django's database models module
from django.db import models


# Create the UniversityCampus database model
class UniversityCampus(models.Model):

    # Store the name of the university campus
    campus_name = models.CharField(max_length=200)

    # Store the state abbreviation using a maximum of 2 characters
    state = models.CharField(max_length=2)

    # Store the unique campus identification number
    campus_id = models.IntegerField()

    # Add the default Django model manager
    objects = models.Manager()

    # Configure the model's display names in Django Admin
    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campuses"

    # Display campus name and state when viewing records
    def __str__(self):
        return f"{self.campus_name} ({self.state})"
