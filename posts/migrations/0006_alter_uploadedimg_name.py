# Generated by Django 4.0.4 on 2022-08-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_uploadedimg_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimg',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
