# Generated by Django 4.2.1 on 2023-06-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_orderitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('sorted', 'Sorted'), ('unsorted', 'Unsorted')], default='unsorted', max_length=30),
        ),
    ]
