# Generated by Django 2.2.2 on 2019-06-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20190629_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='NY', max_length=2),
        ),
    ]
