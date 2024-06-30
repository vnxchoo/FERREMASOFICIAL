from django.db import models



class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre    
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha = models.DateField()
    codigo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.nombre
    
opciones_consultas = [
        [0, "Consulta"],
        [1, "reclamo"],
        [2, "sugerencias"],
        [3, "felicitaciones"]
    ]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta =models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Transferencia(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=20, default='1')
    correo = models.EmailField()
    CodigoP = models.CharField(max_length=50, db_column='Codigo Producto') 
    imagen = models.ImageField(upload_to="productos", null=True)    

    def __str__(self):
        return self.nombre

