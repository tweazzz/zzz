# Generated by Django 5.0.6 on 2024-06-11 11:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_alter_schoolpasport_school_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacherworkload',
            name='classl',
        ),
        migrations.RemoveField(
            model_name='dopurok',
            name='classl',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='classl',
        ),
        migrations.RemoveField(
            model_name='classrooms',
            name='school',
        ),
        migrations.RemoveField(
            model_name='pandikolimpiada_success',
            name='classl',
        ),
        migrations.RemoveField(
            model_name='sport_success',
            name='classl',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='menu',
            name='food_reti',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day_of_week',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='shift',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='city',
            field=models.CharField(choices=[('almaty', 'Алматы'), ('astana', 'Астана'), ('shymkent', 'Шымкент')], default='almaty', max_length=255, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='subject',
            name='double',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subject',
            name='importance',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='is_subgroup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='altynbelgi',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='altynbelgi',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='ring',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.ring'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.subject'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='admin_app.subject'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher2', to='admin_app.teacher'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='typez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.extra_lessons'),
        ),
        migrations.AlterField(
            model_name='dopurokring',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='extra_lessons',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='redcertificate',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='redcertificate',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='ring',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ring',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='ring',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='ring',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.ring'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.subject'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_g2', to='admin_app.subject'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_g2', to='admin_app.teacher'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='typez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.extra_lessons'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='week_day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=20),
        ),
        migrations.AlterField(
            model_name='school',
            name='region',
            field=models.CharField(choices=[('abay', 'Абайская область'), ('akmolinsk', 'Акмолинская область'), ('aktobe', 'Актюбинская область'), ('almaty_region', 'Алматинская область'), ('atyrau', 'Атырауская область'), ('east_kazakhstan', 'Восточно-Казахстанская область'), ('zhambyl', 'Жамбылская область'), ('zhetysu', 'Жетысуская область'), ('west_kazakhstan', 'Западно-Казахстанская область'), ('karaganda', 'Карагандинская область'), ('kostanay', 'Костанайская область'), ('kyzylorda', 'Кызылординская область'), ('mangystau', 'Мангистауская область'), ('pavlodar', 'Павлодарская область'), ('north_kazakhstan', 'Северо-Казахстанская область'), ('turkestan', 'Туркестанская область'), ('ulytau', 'Улытауская область')], max_length=255, null=True, verbose_name='region'),
        ),
        migrations.AlterField(
            model_name='school',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school_administration',
            name='administator_photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='school_administration',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='school_director',
            name='director_photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='school_director',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='schoolpasport',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='slider',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='sport_success',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sport_success',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(choices=[('INVARIANT', 'INVARIANT'), ('VARIANT', 'VARIANT')], default='INVARIANT', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pedagog',
            field=models.CharField(choices=[('Pedagog Sheber', 'Pedagog Sheber'), ('Pedagog Zertteushy', 'Pedagog Zertteushy'), ('Pedagog Sarapshy', 'Pedagog Sarapshy'), ('Pedagog Moderator', 'Pedagog Moderator'), ('Pedagog', 'Pedagog'), ('Pedagog Stazher', 'Pedagog Stazher'), ('Pedagog Zhogary', 'Pedagog Zhogary'), ('Pedagog 1 sanat', 'Pedagog 1 sanat'), ('Pedagog 2 sanat', 'Pedagog 2 sanat'), ('Pedagog sanat zhok', 'Pedagog sanat zhok')], default='Pedagog Sheber', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='teacherworkload',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school'),
        ),
        migrations.AlterField(
            model_name='teacherworkload',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.subject'),
        ),
        migrations.AlterField(
            model_name='teacherworkload',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher'),
        ),
        migrations.CreateModel(
            name='ClassGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=150)),
                ('class_number', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('class_letter', models.CharField(blank=True, max_length=1, null=True)),
                ('osnova_plan', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('osnova_smena', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('dopurok_plan', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('dopurok_smena', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_teacher', to='admin_app.teacher')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'ClassGroups',
            },
        ),
        migrations.AddField(
            model_name='dopurok',
            name='class_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classgroup'),
        ),
        migrations.AddField(
            model_name='pandikolimpiada_success',
            name='class_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classgroup'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='class_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classgroup'),
        ),
        migrations.AddField(
            model_name='sport_success',
            name='class_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classgroup'),
        ),
        migrations.AddField(
            model_name='teacherworkload',
            name='class_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classgroup'),
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_name', models.CharField(max_length=250)),
                ('classroom_number', models.IntegerField(default=1)),
                ('flat', models.IntegerField()),
                ('korpus', models.IntegerField()),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'Classrooms',
            },
        ),
        migrations.AddField(
            model_name='classgroup',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classroom'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classroom'),
        ),
        migrations.AlterField(
            model_name='dopurok',
            name='classroom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom2', to='admin_app.classroom'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_app.classroom'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classroom'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='classroom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom_g2', to='admin_app.classroom'),
        ),
        migrations.AlterField(
            model_name='teacherworkload',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classroom'),
        ),
        migrations.AddField(
            model_name='classgroup',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.nationality'),
        ),
        migrations.AddField(
            model_name='subject',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.nationality'),
        ),
        migrations.CreateModel(
            name='PhotoforNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_photos', to='admin_app.news')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolLessonTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_week', models.CharField(max_length=10)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_per_week', models.IntegerField()),
                ('class_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classgroup')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.classroom')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Classrooms',
        ),
    ]
