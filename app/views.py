from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Producto, Transferencia
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, TransForm
from rest_framework import generics
from .serializers import ProductoSerializer

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from .carrito import Carrito

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje enviado")
    return render(request, 'app/contacto.html', data)

def transferencia(request):
    data = {
        'form': TransForm()  # Instancia del formulario
    }

    if request.method == 'POST':
        formulario = TransForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Transferencia Enviada")
            return redirect('carrito')  # Redirigir a alguna URL después de guardar
        else:
            data['form'] = formulario  # Pasar el formulario con errores de vuelta al contexto

    return render(request, 'app/transferencia/transferencia.html', data)
def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):
    data = {'form': ProductoForm(), 'mensaje': ''}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()  # ¡No olvides los paréntesis para llamar a la función save!
            messages.success(request, "Guardado correctamente")
        else:
            data['form'] = formulario
    return render(request, 'app/producto/agregar.html', data)

def listar_producto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos, 5)
        productos= paginator.page(page)
    except : Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)

    data={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_producto")


    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_producto")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data['form'] = formulario    
    return render(request, 'registration/registro.html', data)

def agregar_producto_car(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto_car(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")
def carrito(request):
    carrito = request.session.get('carrito', {})
    total_carrito = 0
    for key, value in carrito.items():
        value['precio_unitario'] = value['acumulado'] / value['cantidad']
        total_carrito += value['acumulado']
    return render(request, 'app/carrito.html', {'carrito': carrito, 'total_carrito': total_carrito})



class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def lista_transferencias(request):
    transferencias = Transferencia.objects.all()

    context = {
        'transferencias': transferencias,
    }

    return render(request, 'app/transferencia/listaTransferencia.html', context)    