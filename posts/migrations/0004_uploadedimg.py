# Generated by Django 4.0.4 on 2022-08-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_delete_uplodedimgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadedimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]