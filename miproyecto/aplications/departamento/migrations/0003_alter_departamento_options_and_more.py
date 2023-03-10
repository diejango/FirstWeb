# Generated by Django 4.1.5 on 2023-01-25 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_name_alter_departamento_shorname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'verbose_name': 'apartment', 'verbose_name_plural': 'apartments'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shorname')},
        ),
    ]
