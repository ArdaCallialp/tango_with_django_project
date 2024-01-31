from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Corrected field name to 'Title'

# Register the models with the custom admin classes
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
