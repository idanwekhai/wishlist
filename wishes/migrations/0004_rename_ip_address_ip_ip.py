# Generated by Django 3.2.11 on 2022-01-05 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0003_auto_20220105_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='ip_address',
            new_name='ip',
        ),
    ]
