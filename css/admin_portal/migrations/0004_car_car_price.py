# Generated by Django 4.2 on 2023-04-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_portal', '0003_alter_car_user_id_alter_carimage_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_price',
            field=models.IntegerField(null=True),
        ),
    ]
