from django.contrib import admin
from .models import Product, Category

# Register your models here.
class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Product)