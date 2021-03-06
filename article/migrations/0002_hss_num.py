# Generated by Django 2.0.1 on 2018-01-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HSS_NUM',
            fields=[
                ('MSISDN_NO', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('IMSI_NO', models.DecimalField(decimal_places=0, max_digits=20)),
                ('HSS', models.CharField(max_length=50)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['MSISDN_NO'],
            },
        ),
    ]
