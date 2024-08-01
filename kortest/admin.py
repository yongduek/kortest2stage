from django.contrib import admin
# ref: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

from .models import Item, TestSheet, Membership, Answer

# Register your models here.
class TestSheetAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestSheet, TestSheetAdmin)

admin.site.register(Item)
admin.site.register(Membership)
admin.site.register(Answer)
