# Generated by Django 2.2.4 on 2019-08-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190822_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialitem',
            name='page',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]