# Generated by Django 3.0.5 on 2020-04-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200425_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productimage',
            field=models.ImageField(null=True, upload_to='static/img/products'),
        ),
    ]
