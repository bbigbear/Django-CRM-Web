# Generated by Django 4.2.3 on 2023-07-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
