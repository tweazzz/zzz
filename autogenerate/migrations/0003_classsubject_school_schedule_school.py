# Generated by Django 4.2.7 on 2024-04-02 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_alter_schedule_classroom'),
        ('autogenerate', '0002_remove_classsubject_class_room_delete_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='classsubject',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classSubject_school', to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_school', to='admin_app.school'),
        ),
    ]