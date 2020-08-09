# Generated by Django 3.0.8 on 2020-08-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0003_auto_20200806_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.TextField(),
        ),
    ]
