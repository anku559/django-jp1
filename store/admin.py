from django.contrib import admin
from store import models

# Way 1 - With Custom Fields
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price"]
    list_editable = ["unit_price"]
    list_per_page = 10


# Way 2 - With Default Fields
admin.site.register(models.Collection)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10


admin.site.register(models.Customer, CustomerAdmin)
