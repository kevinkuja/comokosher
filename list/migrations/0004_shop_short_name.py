# Generated by Django 3.0.8 on 2020-07-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20200706_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='short_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
