# Generated by Django 2.2.2 on 2019-07-01 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquries', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Inquiry',
        ),
        migrations.RenameField(
            model_name='inquiry',
            old_name='contact_date',
            new_name='Inquiry_date',
        ),
    ]
