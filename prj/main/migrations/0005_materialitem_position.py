# Generated by Django 2.2.4 on 2019-08-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_materialitem_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialitem',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]