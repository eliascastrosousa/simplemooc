# Generated by Django 4.2.4 on 2023-08-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='descripton',
            field=models.TextField(blank=True, max_length=255, verbose_name='Descrição'),
        ),
    ]
