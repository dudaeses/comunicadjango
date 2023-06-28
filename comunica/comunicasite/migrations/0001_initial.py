# Generated by Django 4.1.7 on 2023-06-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('comentario', models.TextField()),
                ('publicado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]