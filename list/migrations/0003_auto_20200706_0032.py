# Generated by Django 3.0.8 on 2020-07-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20200705_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='instagram',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]