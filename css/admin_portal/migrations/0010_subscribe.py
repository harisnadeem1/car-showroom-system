# Generated by Django 4.2 on 2023-05-02 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_portal', '0009_status_alter_buyer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=70)),
            ],
        ),
    ]
