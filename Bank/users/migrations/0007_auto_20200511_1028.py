# Generated by Django 3.0.6 on 2020-05-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200511_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transactionID',
            field=models.CharField(default='78I06DxU6u3anix', max_length=15, unique=True),
        ),
    ]
