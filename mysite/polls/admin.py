from django.contrib import admin

# Register your models here.
from .models import Request, Output

admin.site.register(Request)
admin.site.register(Output)

