from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro,  agregar_producto_car, eliminar_producto_car,restar_producto, limpiar_carrito, carrito, ProductoListCreate, transferencia
urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('listar_producto', listar_producto, name="listar_producto"),
   path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
   path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
   path('registro/', registro, name="registro"), 
   path('transferencia/', transferencia, name="transferencia"), 

    path('agregar/<int:producto_id>/', agregar_producto_car, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto_car, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('carrito/', carrito, name='carrito'),
     path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
     
]
