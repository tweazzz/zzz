# Generated by Django 4.2.7 on 2024-02-05 09:43

import admin_app.models
import colorfield.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltynBelgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('student_success', models.CharField(max_length=250)),
                ('endyear', models.CharField(default='2011-2022', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'AltynBelgi',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=150)),
                ('class_number', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('language', models.CharField(choices=[('KZ', 'KZ'), ('RU', 'RU')], default='KZ', max_length=20)),
                ('osnova_plan', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('osnova_smena', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('dopurok_plan', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('dopurok_smena', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_name', models.CharField(max_length=250)),
                ('classroom_number', models.IntegerField(default=1)),
                ('flat', models.IntegerField()),
                ('korpus', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Classrooms',
            },
        ),
        migrations.CreateModel(
            name='DopUrok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DopUrokRing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('smena', models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'), (3, '3 смена'), (4, '4 смена')], default=1)),
                ('number', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)])),
                ('start_time', models.TimeField(default=datetime.time(0, 0))),
                ('end_time', models.TimeField(default=datetime.time(0, 0))),
            ],
        ),
        migrations.CreateModel(
            name='Extra_Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_full_name', models.CharField(max_length=200)),
                ('type_color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='Выберите цвет')),
            ],
            options={
                'verbose_name_plural': 'Extra Lessons',
            },
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('job_characteristic', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Job History',
            },
        ),
        migrations.CreateModel(
            name='Kruzhok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kruzhok_name', models.CharField(max_length=250)),
                ('photo', models.ImageField(null=True, upload_to='main/static/img')),
                ('purpose', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=20)),
                ('start_end_time', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=250)),
                ('food_reti', models.CharField(max_length=150)),
                ('food_sostav', models.TextField()),
                ('vihod_1', models.CharField(max_length=100, null=True)),
                ('vihod_2', models.CharField(max_length=100, null=True)),
                ('vihod_3', models.CharField(max_length=100, null=True)),
                ('week_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('manual', 'Manual')], default='manual', max_length=10)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='news_qrcodes/')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Oner_Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('student_success', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Pride of the School Oner',
            },
        ),
        migrations.CreateModel(
            name='PandikOlimpiada_Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('student_success', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Pride of the School Olimpiada',
            },
        ),
        migrations.CreateModel(
            name='PhotoforNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RedCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('student_success', models.CharField(max_length=250)),
                ('endyear', models.CharField(default='2011-2022', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Red Certificate',
            },
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('smena', models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'), (3, '3 смена'), (4, '4 смена')], default=1)),
                ('number', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)])),
                ('start_time', models.TimeField(default=datetime.time(0, 0))),
                ('end_time', models.TimeField(default=datetime.time(0, 0))),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_kz_name', models.CharField(max_length=255, verbose_name='school_full_name')),
                ('school_ru_name', models.CharField(max_length=255, null=True, verbose_name='school_full_name')),
                ('school_eng_name', models.CharField(max_length=255, null=True, verbose_name='school_full_name')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('region', models.CharField(choices=[('abay', 'Абайская область'), ('akmolinsk', 'Акмолинская область'), ('aktobe', 'Актюбинская область'), ('almaty_region', 'Алматинская область'), ('atyrau', 'Атырауская область'), ('east_kazakhstan', 'Восточно-Казахстанская область'), ('zhambyl', 'Жамбылская область'), ('zhetysu', 'Жетысуская область'), ('west_kazakhstan', 'Западно-Казахстанская область'), ('karaganda', 'Карагандинская область'), ('kostanay', 'Костанайская область'), ('kyzylorda', 'Кызылординская область'), ('mangystau', 'Мангистауская область'), ('pavlodar', 'Павлодарская область'), ('north_kazakhstan', 'Северо-Казахстанская область'), ('turkestan', 'Туркестанская область'), ('ulytau', 'Улытауская область')], max_length=255, null=True, verbose_name='region')),
                ('city', models.CharField(choices=[('almaty', 'Алматы'), ('astana', 'Астана'), ('shymkent', 'Шымкент')], default='almaty', max_length=255, null=True, verbose_name='city')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('timezone', models.CharField(choices=[('GMT+5', 'GMT+5'), ('GMT+6', 'GMT+6')], default='GMT+5', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], default='EASY', max_length=20)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('photo3x4', models.ImageField(blank=True, null=True, upload_to='')),
                ('subject', models.CharField(max_length=250, null=True)),
                ('pedagog', models.CharField(choices=[('Pedagog Sheber', 'Pedagog Sheber'), ('Pedagog  Zertteushy', 'Pedagog  Zertteushy'), ('Pedagog Sarapshy', 'Pedagog Sarapshy'), ('Pedagog Moderator', 'Pedagog Moderator'), ('Pedagog', 'Pedagog'), ('Pedagog  Stazher', 'Pedagog  Stazher'), ('Pedagog  Zhogary', 'Pedagog  Zhogary'), ('Pedagog  1 sanat', 'Pedagog  1 sanat'), ('Pedagog  2 sanat', 'Pedagog  2 sanat'), ('Pedagog sanat zhok', 'Pedagog sanat zhok')], default='Pedagog Sheber', max_length=20)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='TeacherWorkload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50)])),
                ('classl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.class')),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.classrooms')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Sport_Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('student_success', models.TextField()),
                ('classl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.class')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'Pride of the School Sport',
            },
        ),
        migrations.CreateModel(
            name='SpecialityHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField()),
                ('speciality_university', models.TextField()),
                ('mamandygy', models.CharField(max_length=150, null=True)),
                ('degree', models.CharField(choices=[('Среднее', 'Среднее'), ('Высшее', 'Высшее')], default='Высшее', max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.teacher')),
            ],
            options={
                'verbose_name_plural': 'Speciality History',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_name', models.CharField(max_length=355)),
                ('slider_photo', models.ImageField(upload_to='')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='schoolPasport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('established', models.IntegerField(default=2008)),
                ('school_address', models.CharField(max_length=250)),
                ('amount_of_children', models.IntegerField()),
                ('ul_sany', models.IntegerField()),
                ('kiz_sany', models.IntegerField()),
                ('school_lang', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=250)),
                ('vmestimost', models.IntegerField()),
                ('dayarlyk_class_number', models.IntegerField(null=True)),
                ('dayarlyk_student_number', models.IntegerField(null=True)),
                ('number_of_students', models.IntegerField()),
                ('number_of_classes', models.IntegerField()),
                ('number_of_1_4_students', models.IntegerField()),
                ('number_of_1_4_classes', models.IntegerField()),
                ('number_of_5_9_students', models.IntegerField()),
                ('number_of_5_9_classes', models.IntegerField()),
                ('number_of_10_11_students', models.IntegerField()),
                ('number_of_10_11_classes', models.IntegerField()),
                ('amount_of_family', models.IntegerField()),
                ('amount_of_parents', models.IntegerField()),
                ('all_pedagog_number', models.IntegerField(null=True)),
                ('pedagog_sheber', models.IntegerField(null=True)),
                ('pedagog_zertteushy', models.IntegerField(null=True)),
                ('pedagog_sarapshy', models.IntegerField(null=True)),
                ('pedagog_moderator', models.IntegerField(null=True)),
                ('pedagog', models.IntegerField(null=True)),
                ('pedagog_stazher', models.IntegerField(null=True)),
                ('pedagog_zhogary', models.IntegerField(null=True)),
                ('pedagog_1sanat', models.IntegerField(null=True)),
                ('pedagog_2sanat', models.IntegerField(null=True)),
                ('pedagog_sanat_zhok', models.IntegerField(null=True)),
                ('school_history', models.TextField(null=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'School Pasport',
            },
        ),
        migrations.CreateModel(
            name='SchoolMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.FileField(upload_to='uploads/', validators=[admin_app.models.validate_file_extension])),
                ('flat1', models.FileField(upload_to='uploads/', validators=[admin_app.models.validate_file_extension])),
                ('flat2', models.FileField(blank=True, null=True, upload_to='uploads/', validators=[admin_app.models.validate_file_extension])),
                ('flat3', models.FileField(blank=True, null=True, upload_to='uploads/', validators=[admin_app.models.validate_file_extension])),
                ('flat4', models.FileField(blank=True, null=True, upload_to='uploads/', validators=[admin_app.models.validate_file_extension])),
                ('flat5', models.FileField(blank=True, null=True, upload_to='uploads/', validators=[admin_app.models.validate_file_extension])),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'SchoolMap',
            },
        ),
        migrations.CreateModel(
            name='School_SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('Youtube', 'Youtube')], default='Youtube', max_length=10)),
                ('account_name', models.CharField(max_length=250)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='social_media_qrcodes/')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'School Social Media',
            },
        ),
        migrations.CreateModel(
            name='School_Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=100)),
                ('director_photo', models.ImageField(upload_to='')),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'School Director',
            },
        ),
        migrations.CreateModel(
            name='School_Administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrator_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('administator_photo', models.ImageField(upload_to='')),
                ('position', models.CharField(max_length=100)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.school')),
            ],
            options={
                'verbose_name_plural': 'School Administration',
            },
        ),
    ]
