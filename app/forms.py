from django import forms
from .models import Contacto, Producto, Transferencia
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):
    class Meta: 
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = '__all__'
        widgets = {
            "fecha": forms.SelectDateWidget()
        }



class TransForm(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ['nombre', 'rut', 'correo', 'CodigoP', 'imagen']  # Incluye el campo imagen


class CustomUserCreationForm(UserCreationForm):
    pass      