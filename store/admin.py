from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
  list_editable = ['unit_price']
  list_select_related = ['collection']
  list_per_page = 10

  @admin.display(ordering='inventory')
  def  inventory_status(self, product):
    if product.inventory < 10:
      return 'Low'
    return 'Ok'

  def collection_title(self, product):
    return product.collection.title

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'membership']
  ordering = ['first_name', 'last_name']
  list_editable = ['membership']
  list_per_page = 10

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ['title']
  ordering = ['title']
  list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ['id', 'placed_at', 'customer']
  list_select_related = ['customer']
  list_per_page = 10
