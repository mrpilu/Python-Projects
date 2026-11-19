
# Import Django's admin module
from django.contrib import admin

# Import the UniversityCampus model
from .models import UniversityCampus

# Register UniversityCampus with Django Admin
admin.site.register(UniversityCampus)
