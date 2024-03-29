# Generated by Django 4.2.7 on 2024-03-26 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedule',
            name='classl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.class'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.classrooms'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='classroom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classroom_g2', to='admin_app.classrooms'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='ring',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.ring'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.subject'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject_g2', to='admin_app.subject'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_g2', to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='typez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.extra_lessons'),
        ),
        migrations.AddField(
            model_name='ring',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='redcertificate',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='pandikolimpiada_success',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='oner_success',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='news',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='menu',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='kruzhok',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='admin_app.kruzhok'),
        ),
        migrations.AddField(
            model_name='kruzhok',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='kruzhok',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='jobhistory',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='extra_lessons',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='dopurokring',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='classl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.class'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.classrooms'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='classroom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classroom2', to='admin_app.classrooms'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='ring',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.dopurokring'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.subject'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject2', to='admin_app.subject'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher2', to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='typez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.extra_lessons'),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='class',
            name='class_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_teacher', to='admin_app.teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classrooms'),
        ),
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AddField(
            model_name='altynbelgi',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.school'),
        ),
        migrations.AlterUniqueTogether(
            name='school_socialmedia',
            unique_together={('school', 'type')},
        ),
    ]
