from django.contrib import admin
from categories import models

# admin.site.register(models.categories)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('categori',)}
    list_display=['categori','slug']

admin.site.register(models.Category,CategoryAdmin)