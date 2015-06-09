from django.contrib import admin
from stall.models import (ItemPicture, Item, Seller, ValidateCode)

def make_validated(modeladmin, request, queryset):
    queryset.update(status=3)

make_validated.short_description = "标记选择的卖家审核通过"

def make_invalidated(modeladmin, request, queryset):
    queryset.update(status=4)

make_invalidated.short_description = "标记选择的卖家审核不通过"

class SellerAdmin(admin.ModelAdmin):
    ordering = ['signup_datetime']
    actions = [make_validated, make_invalidated]

admin.site.register(ItemPicture)
admin.site.register(Item)
admin.site.register(Seller, SellerAdmin)
admin.site.register(ValidateCode)
