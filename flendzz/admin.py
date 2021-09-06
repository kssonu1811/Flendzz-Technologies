from django.contrib import admin
from .models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ("id","name","roll_number","date_of_birth","marks")
    list_display_links = ("id","roll_number","name")
    search_fields = ("name","roll_number")
    list_per_page = 25
admin.site.register(student, studentAdmin)