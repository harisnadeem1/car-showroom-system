# Generated by Django 4.2 on 2023-05-02 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_portal', '0004_car_car_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_id', models.AutoField(primary_key=True, serialize=False)),
                ('buyer_name', models.CharField(max_length=50)),
                ('buyer_address', models.CharField(max_length=50)),
                ('buyer_contact', models.CharField(max_length=50)),
                ('buyer_payment_method', models.CharField(max_length=50)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_portal.car', verbose_name='buy_car')),
            ],
        ),
    ]
