# Generated by Django 4.2.8 on 2023-12-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('item_price', models.IntegerField()),
                ('is_epic', models.BooleanField()),
            ],
        ),
    ]
