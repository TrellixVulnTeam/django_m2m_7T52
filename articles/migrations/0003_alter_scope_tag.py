# Generated by Django 3.2.6 on 2021-08-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210825_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.CharField(max_length=30),
        ),
    ]
