# Generated by Django 3.2.7 on 2021-10-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
