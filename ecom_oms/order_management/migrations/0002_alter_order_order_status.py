# Generated by Django 4.2.1 on 2023-06-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.TextField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Refunded', 'Refunded'), ('Failed', 'Failed')], db_index=True, default='Pending'),
        ),
    ]
