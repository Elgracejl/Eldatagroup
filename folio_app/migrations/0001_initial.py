# Generated by Django 5.1.1 on 2024-09-19 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('framework', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/')),
                ('create', models.DateField()),
                ('Update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='My_portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='my_portfolio/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folio_app.category')),
            ],
        ),
    ]
