# Generated by Django 3.2.4 on 2021-07-14 17:40

from django.db import migrations, models
import uploadvideo.validator


class Migration(migrations.Migration):

    dependencies = [
        ('uploadvideo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='video',
            field=models.FileField(upload_to='video/', validators=[uploadvideo.validator.file_size]),
        ),
    ]
