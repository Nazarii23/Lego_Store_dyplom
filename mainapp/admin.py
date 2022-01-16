from django.contrib import admin
from django import  forms
# Register your models here.
from .models import *





class LegoCatrgoryChoiceField(forms.ModelChoiceField):
    pass


class LegoAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return LegoCatrgoryChoiceField(Category.objects.filter(slug='legozestawy'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(LegoZestawy, LegoAdmin)
admin.site.register(LegoFigure)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartProduct)