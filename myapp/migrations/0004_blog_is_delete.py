# Generated by Django 2.1.4 on 2019-01-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190104_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]