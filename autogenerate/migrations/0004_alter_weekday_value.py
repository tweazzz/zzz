# Generated by Django 4.2.7 on 2024-04-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autogenerate', '0003_classsubject_school_schedule_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='value',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=20),
        ),
    ]