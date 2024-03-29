# Generated by Django 4.2.7 on 2024-03-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autogenerate', '0002_remove_weekday_class_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekday',
            name='class_hours',
            field=models.ManyToManyField(related_name='week_days', to='autogenerate.classhour'),
        ),
    ]
