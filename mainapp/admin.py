from django.contrib import admin
from django import  forms
# Register your models here.
from .models import *
from django.forms import ModelChoiceField






class LegoZestawyAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='lego_zestawy'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class LegoFiguresAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Lego_figures'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(LegoZestawy, LegoZestawyAdmin)
admin.site.register(LegoFigure, LegoFiguresAdmin)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartProduct)