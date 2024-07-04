from django.contrib import admin
from .models import CarModel, BrandModel, Buy, commentsModel


# Register your models here.

admin.site.register(CarModel)
# admin.site.register(BrandModel)
admin.site.register(Buy)

class Brand(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(BrandModel, Brand)
admin.site.register(commentsModel)
