# Generated by Django 4.1.5 on 2023-01-26 17:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]