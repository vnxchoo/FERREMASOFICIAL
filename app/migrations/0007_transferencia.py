# Generated by Django 5.0.6 on 2024-06-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_itemcarrito_carrito_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('codigoP', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]
