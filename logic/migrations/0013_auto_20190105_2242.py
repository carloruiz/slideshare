# Generated by Django 2.1.2 on 2019-01-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0012_auto_20190105_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide_id',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
