# Generated by Django 2.2.4 on 2020-03-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]