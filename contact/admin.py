from django.contrib import admin
from .models import Contact

# Register your models here.

admin.site.register(Contact)

admin.site.site_header = 'Nollytics'