# Generated by Django 5.0 on 2023-12-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='stock code'),
        ),
    ]