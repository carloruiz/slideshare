# Generated by Django 2.1.2 on 2019-01-05 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0011_auto_20190105_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='logic.Slide_id'),
        ),
    ]
