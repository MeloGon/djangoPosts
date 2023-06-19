from django.contrib import admin
from posts.models import PosT

# Register your models here.
@admin.register(PosT)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']