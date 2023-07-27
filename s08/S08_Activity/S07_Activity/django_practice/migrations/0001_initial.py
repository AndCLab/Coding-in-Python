# Generated by Django 4.1.5 on 2023-04-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
