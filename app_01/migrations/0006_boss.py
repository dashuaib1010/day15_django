# Generated by Django 5.1.3 on 2024-12-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0005_taskinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名字')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('img', models.CharField(max_length=128, verbose_name='头像')),
            ],
        ),
    ]