# Generated by Django 3.2.7 on 2021-10-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
