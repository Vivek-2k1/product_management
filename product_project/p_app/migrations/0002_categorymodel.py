# Generated by Django 4.1.5 on 2023-06-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('products', models.ManyToManyField(to='p_app.productmodel')),
            ],
        ),
    ]
