# Generated by Django 4.0 on 2022-02-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilephoto',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilePhotos'),
        ),
    ]
