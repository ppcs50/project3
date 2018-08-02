from django.contrib import admin

from .models import Type, Size, Style, Topping, Pizza, Sub, SaladPasta, Dinplat, Cart, Subname, Dinplatname, Subtopping

# Register your models here.
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Style)
admin.site.register(Topping)
admin.site.register(Subname)
admin.site.register(Subtopping)
admin.site.register(Dinplatname)
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(SaladPasta)
admin.site.register(Dinplat)
admin.site.register(Cart)