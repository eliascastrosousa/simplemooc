# Generated by Django 4.2.4 on 2023-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                ("slug", models.SlugField(verbose_name="Atalho")),
                (
                    "descripton",
                    models.TextField(
                        blank=True, max_length=255, verbose_name="Descrição"
                    ),
                ),
                ("about", models.TextField(blank=True, verbose_name="Sobre o Curso")),
                (
                    "start_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Início"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="courses/images",
                        verbose_name="Imagem",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
            ],
            options={
                "verbose_name": "Curso",
                "verbose_name_plural": "Cursos",
            },
        ),
    ]
