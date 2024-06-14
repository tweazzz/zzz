# Generated by Django 5.0.6 on 2024-06-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_alter_teachersubject_classroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='food_reti',
        ),
        migrations.AddField(
            model_name='school',
            name='school_map',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='week_day',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='school',
            name='region',
            field=models.CharField(choices=[('almaty', 'almaty'), ('astana', 'astana'), ('shymkent', 'shymkent'), ('abay_oblast', 'abay_oblast'), ('akmolinsk_oblast', 'akmolinsk_oblast'), ('aktobe_oblast', 'aktobe_oblast'), ('almaty_region', 'almaty_region'), ('atyrau_oblast', 'atyrau_oblast'), ('east_kazakhstan_oblast', 'east_kazakhstan_oblast'), ('zhambyl_oblast', 'zhambyl_oblast'), ('zhetysu_oblast', 'zhetysu_oblast'), ('west_kazakhstan_oblast', 'west_kazakhstan_oblast'), ('karaganda_oblast', 'karaganda_oblast'), ('kostanay_oblast', 'kostanay_oblast'), ('kyzylorda_oblast', 'kyzylorda_oblast'), ('mangystau_oblast', 'mangystau_oblast'), ('pavlodar_oblast', 'pavlodar_oblast'), ('north_kazakhstan_oblast', 'north_kazakhstan_oblast'), ('turkestan_oblast', 'turkestan_oblast'), ('ulytau_oblast', 'ulytau_oblast')], max_length=255, null=True, verbose_name='region'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pedagog',
            field=models.CharField(blank=True, choices=[('pedagog_sheber', 'pedagog_sheber'), ('pedagog_zertteushy', 'pedagog_zertteushy'), ('pedagog_sarapshy', 'pedagog_sarapshy'), ('pedagog_moderator', 'pedagog_moderator'), ('pedagog', 'pedagog'), ('pedagog_stazher', 'pedagog_stazher'), ('pedagog_zhogary', 'pedagog_zhogary'), ('pedagog1sanat', 'pedagog1sanat'), ('pedagog2sanat', 'pedagog2sanat'), ('pedagog_sanat_zhok', 'pedagog_sanat_zhok')], default='pedagog', max_length=200, null=True),
        ),
    ]