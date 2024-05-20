from django.contrib import admin
from .models import Marca, Producto, Categoria, Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","marca","precio","nuevo",)
    list_editable=("precio",)
    search_fields=("nombre",)
    list_filter= ("categoria", "marca",)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)