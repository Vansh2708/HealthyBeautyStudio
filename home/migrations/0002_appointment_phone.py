# Generated by Django 5.2.3 on 2025-07-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone',
            field=models.CharField(default='00000000000', max_length=15),
            preserve_default=False,
        ),
    ]
