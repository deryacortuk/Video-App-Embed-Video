# Generated by Django 3.2.4 on 2021-07-14 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadvideo', '0002_alter_videomodel_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videomodel',
            options={'ordering': ['-created_date']},
        ),
    ]
