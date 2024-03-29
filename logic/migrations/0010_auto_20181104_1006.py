# Generated by Django 2.1.2 on 2018-11-04 15:06

from django.db import migrations, models
import logic.models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0009_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slide',
            name='thumbnail',
            field=models.ImageField(upload_to=logic.models.Slide.upload_path_handler),
        ),
    ]
