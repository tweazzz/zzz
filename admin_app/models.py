from django.db import models
from colorfield.fields import ColorField

import datetime
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class School(models.Model):
    school_kz_name = models.CharField('school_full_name', max_length=255)
    school_ru_name = models.CharField('school_full_name', max_length=255, null=True)
    school_eng_name = models.CharField('school_full_name', max_length=255, null=True)
    url = models.CharField('url', max_length=255)
    city = models.CharField('city', max_length=255)
    logo = models.ImageField(blank=True, null=True)
    GMT_5 = 'GMT+5'
    GMT_6 = 'GMT+6'
    timezone_choices = [
        (GMT_5, 'GMT+5'),
        (GMT_6, 'GMT+6'),
    ]
    timezone = models.CharField(
        max_length=20,
        choices=timezone_choices,
        default=GMT_5,
    )
    user = models.OneToOneField('auth_user.User', on_delete=models.CASCADE, blank=True, null=True, related_name='school_user')

    class Meta:
        verbose_name_plural = 'Schools'

    def __str__(self):
        return f'{self.school_kz_name}'

class Classrooms(models.Model):
    classroom_name = models.CharField(max_length=250)
    classroom_number = models.IntegerField(default=1)
    flat = models.IntegerField()
    korpus = models.IntegerField()
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Classrooms'

    def __str__(self):
        return f'{self.classroom_name}'

class Teacher(models.Model):
    full_name = models.CharField(max_length=250)
    photo3x4 = models.ImageField(null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=250, null=True)
    pedagog_sheber = 'Pedagog Sheber'
    pedagog_zertteushy = 'Pedagog  Zertteushy'
    pedagog_sarapshy = 'Pedagog Sarapshy'
    pedagog_moderator = 'Pedagog Moderator'
    pedagog = 'Pedagog'
    pedagog_stazher = 'Pedagog  Stazher'
    pedagog_zhogary = 'Pedagog  Zhogary'
    pedagog1sanat = 'Pedagog  1 sanat'
    pedagog2sanat = 'Pedagog  2 sanat'
    pedagog_sanat_zhok = 'Pedagog sanat zhok'
    pedagog_choices = [
        (pedagog_sheber, 'Pedagog Sheber'),
        (pedagog_zertteushy, 'Pedagog  Zertteushy'),
        (pedagog_sarapshy, 'Pedagog Sarapshy'),
        (pedagog_moderator, 'Pedagog Moderator'),
        (pedagog, 'Pedagog'),
        (pedagog_stazher, 'Pedagog  Stazher'),
        (pedagog_zhogary, 'Pedagog  Zhogary'),
        (pedagog1sanat, 'Pedagog  1 sanat'),
        (pedagog2sanat, 'Pedagog  2 sanat'),
        (pedagog_sanat_zhok, 'Pedagog sanat zhok'),
    ]
    pedagog = models.CharField(
        max_length=20,
        choices=pedagog_choices,
        default=pedagog_sheber,
    )

    class Meta:
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f'{self.full_name}'

class Class(models.Model):
    class_name = models.CharField(max_length=150)
    class_number = models.CharField(max_length=255, editable=False, null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')
    KZ = 'KZ'
    RU = 'RU'
    lang_choices = [
        (KZ, 'KZ'),
        (RU, 'RU'),
    ]
    language = models.CharField(
        max_length=20,
        choices=lang_choices,
        default=KZ,
    )
    osnova_plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)],null=True)
    osnova_smena = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 5)],null=True)
    dopurok_plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)],null=True)
    dopurok_smena = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 5)],null=True)

    def save(self, *args, **kwargs):
        if self.class_name:
            numbers = [int(s) for s in self.class_name if s.isdigit()]
            self.class_number = ''.join(map(str, numbers))
            self.class_name = self.class_name.strip()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f'{self.class_name}'

class TeacherWorkload(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 51)])
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.teacher} Workload"



class Ring(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 10)])
    smena = models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'),(3, '3 смена'),(4, '4 смена')], default=1)
    number = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)])
    start_time = models.TimeField(default=datetime.time(0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0))
    def __str__(self):
        return f'{self.start_time}-{self.end_time}'

class DopUrokRing(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 10)])
    smena = models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'),(3, '3 смена'),(4, '4 смена')], default=1)
    number = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)])
    start_time = models.TimeField(default=datetime.time(0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0))
    def __str__(self):
        return f'{self.start_time}-{self.end_time}'


class Schedule(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    Saturday = "6"
    WEEK_DAY_CHOICES = [
        (Monday, "1"),
        (Tuesday, "2"),
        (Wednesday, "3"),
        (Thursday, "4"),
        (Friday, "5"),
        (Saturday, "6")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    ring = models.ForeignKey('Ring', on_delete=models.CASCADE,null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)
    teacher2 = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True,blank=True, related_name='teacher_g2')
    classroom2 = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True,blank=True, related_name='classroom_g2')
    subject2 = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True, related_name='subject_g2')
    typez = models.ForeignKey('Extra_Lessons', on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return f'{self.school} {self.classl} - {self.week_day}'

class DopUrok(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    Saturday = "6"
    WEEK_DAY_CHOICES = [
        (Monday, "1"),
        (Tuesday, "2"),
        (Wednesday, "3"),
        (Thursday, "4"),
        (Friday, "5"),
        (Saturday, "6")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    ring = models.ForeignKey('Ring', on_delete=models.CASCADE,null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)
    teacher2 = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True,blank=True, related_name='teacher2')
    classroom2 = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True,blank=True, related_name='classroom2')
    subject2 = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True, related_name='subject2')
    typez = models.ForeignKey('Extra_Lessons', on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return f'{self.school} {self.classl} - {self.week_day}'



class Menu(models.Model):
    food_name = models.CharField(max_length=250)
    food_reti = models.CharField(max_length=150)
    food_sostav = models.TextField()
    vihod_1 = models.CharField(max_length=100, null=True)
    vihod_2 = models.CharField(max_length=100, null=True)
    vihod_3 = models.CharField(max_length=100, null=True)
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    Saturday = "6"
    WEEK_DAY_CHOICES = [
        (Monday, "1"),
        (Tuesday, "2"),
        (Wednesday, "3"),
        (Thursday, "4"),
        (Friday, "5"),
        (Saturday, "6")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    school = models.ForeignKey('School', on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.food_name}'

class Slider(models.Model):
    slider_name = models.CharField(max_length=355)
    slider_photo = models.ImageField()
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Slider'

    def __str__(self):
        return f'{self.slider_name}'

class News(models.Model):
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    MANUAL = 'manual'
    SOCIAL_MEDIA_CHOICES = [
        (INSTAGRAM, 'Instagram'),
        (FACEBOOK, 'Facebook'),
        (MANUAL, 'Manual'),
    ]
    date = models.DateField()
    text = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='news')
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default=MANUAL,
    )
    photos = models.ManyToManyField('PhotoforNews', related_name='news_photos', blank=True)
    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.date}  {self.school} news'

class PhotoforNews(models.Model):
    image = models.ImageField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_photos',null=True)


class Subject(models.Model):
    full_name = models.CharField(max_length=250)
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'
    type_choices = [
        (EASY, 'EASY'),
        (MEDIUM, 'MEDIUM'),
        (HARD, 'HARD'),
    ]
    type = models.CharField(
        max_length=20,
        choices=type_choices,
        default=EASY,
    )
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f'{self.full_name}'



# =============== School Pasport ============================================================

class schoolPasport(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    photo = models.ImageField(null=True)
    established = models.IntegerField(default=2008)
    school_address = models.CharField(max_length=250)
    amount_of_children = models.IntegerField()
    ul_sany = models.IntegerField()
    kiz_sany = models.IntegerField()
    school_lang = models.CharField(max_length=255)
    status = models.CharField(max_length=250)
    vmestimost = models.IntegerField()
    dayarlyk_class_number = models.IntegerField(null=True)
    dayarlyk_student_number = models.IntegerField(null=True)
    number_of_students = models.IntegerField()
    number_of_classes = models.IntegerField()
    number_of_1_4_students = models.IntegerField()
    number_of_1_4_classes = models.IntegerField()
    number_of_5_9_students = models.IntegerField()
    number_of_5_9_classes = models.IntegerField()
    number_of_10_11_students = models.IntegerField()
    number_of_10_11_classes = models.IntegerField()
    amount_of_family = models.IntegerField()
    amount_of_parents = models.IntegerField()
    all_pedagog_number = models.IntegerField(null=True)
    pedagog_sheber = models.IntegerField(null=True)
    pedagog_zertteushy = models.IntegerField(null=True)
    pedagog_sarapshy = models.IntegerField(null=True)
    pedagog_moderator = models.IntegerField(null=True)
    pedagog = models.IntegerField(null=True)
    pedagog_stazher = models.IntegerField(null=True)
    pedagog_zhogary = models.IntegerField(null=True)
    pedagog_1sanat = models.IntegerField(null=True)
    pedagog_2sanat = models.IntegerField(null=True)
    pedagog_sanat_zhok = models.IntegerField(null=True)
    school_history = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'School Pasport'

    def __str__(self):
        return f'{self.school} + School Passport'

class School_SocialMedia(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    youtube = 'Youtube'
    SOCIAL_MEDIA_CHOICES = [
        (INSTAGRAM, 'Instagram'),
        (FACEBOOK, 'Facebook'),
        (youtube, 'Youtube'),
    ]
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default=youtube,
    )
    account_name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "School Social Media"

    def __str__(self):
        return f'{self.school} Social Media {self.type}'


class School_Administration(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    administrator_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    administator_photo = models.ImageField()
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "School Administration"

    def __str__(self):
        return f'{self.school} - {self.administrator_name}'


# =================== Pride_of_the_School =====================================================

class Sport_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(null=True)
    student_success = models.TextField()
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Sport"

    def __str__(self):
        return f'{self.fullname}'

class Oner_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(null=True)
    student_success = models.TextField()
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Oner"

    def __str__(self):
        return f'{self.fullname}'

class PandikOlimpiada_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(null=True)
    student_success = models.TextField()
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Olimpiada"

    def __str__(self):
        return f'{self.fullname}'

class RedCertificate(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.CharField(max_length=250)
    endyear = models.CharField(max_length=10, default="2011-2022")

    class Meta:
        verbose_name_plural = "Red Certificate"

    def __str__(self):
        return f'{self.fullname}, {self.school}, {self.endyear}'

class AltynBelgi(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.CharField(max_length=250)
    endyear = models.CharField(max_length=10, default="2011-2022")

    class Meta:
        verbose_name_plural = "AltynBelgi"

    def __str__(self):
        return f'{self.fullname}, {self.school}, {self.endyear}'

# class School_History(models.Model):
#     school_photo = models.ImageField(upload_to='main/static/img')
#     school_full_name = models.CharField(max_length=100)
#     established =  models.DateField(verbose_name='Established')
#     school_directors = models.TextField()
#     school = models.ForeignKey('School', on_delete=models.CASCADE, null = True)

#     class Meta:
#         verbose_name_plural = "School History"

#     def __str__(self):
#         return f'{self.school_full_name} + History'

class School_Director(models.Model):
    director_name = models.CharField(max_length=100)
    director_photo = models.ImageField()
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "School Director"

    def __str__(self):
        return f'{self.director_name}'

class Extra_Lessons(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    type_full_name = models.CharField(max_length=200)
    type_color = ColorField(verbose_name='Выберите цвет')

    class Meta:
        verbose_name_plural = "Extra Lessons"

    def __str__(self):
        return f'{self.type_full_name}'



# ====================================================
#             History

class JobHistory(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    job_characteristic = models.TextField()

    class Meta:
        verbose_name_plural = "Job History"

    def __str__(self):
        return f'{self.teacher} History'


class SpecialityHistory(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=False)
    end_date = models.DateField()
    speciality_university = models.TextField()
    srednee = "Среднее"
    Viswee = "Высшее"
    degree_choices= [
        (srednee, "Среднее"),
        (Viswee, "Высшее"),
    ]
    mamandygy = models.CharField(max_length=150, null=True)
    degree = models.CharField(
        max_length=20,
        choices=degree_choices,
        default=Viswee,
    )


    class Meta:
        verbose_name_plural = "Speciality History"

    def __str__(self):
        return f'{self.teacher} Speciality History'


    # ======================================================================================

class Kruzhok(models.Model):
    kruzhok_name = models.CharField(max_length=250)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='main/static/img',null=True)
    purpose = models.CharField(max_length=500)
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    Saturday = "6"
    WEEK_DAY_CHOICES = [
        (Monday, "1"),
        (Tuesday, "2"),
        (Wednesday, "3"),
        (Thursday, "4"),
        (Friday, "5"),
        (Saturday, "6")
    ]

    def __str__(self):
        return f'{self.kruzhok_name} - {self.school}'

class Lesson(models.Model):
    kruzhok = models.ForeignKey(Kruzhok, on_delete=models.CASCADE, related_name='lessons')
    week_day = models.CharField(
        max_length=20,
        choices=Kruzhok.WEEK_DAY_CHOICES,
        default=Kruzhok.Monday,
    )
    start_end_time = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.kruzhok.kruzhok_name} - {self.week_day} {self.start_end_time}'
    

class Notifications(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f'{self.school} + {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg']

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please upload a valid image or SVG file.')
    
class SchoolMap(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    map = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    flat1 = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    flat2 = models.FileField(upload_to='uploads/', validators=[validate_file_extension], null=True, blank=True)
    flat3 = models.FileField(upload_to='uploads/', validators=[validate_file_extension], null=True, blank=True)
    flat4 = models.FileField(upload_to='uploads/', validators=[validate_file_extension], null=True, blank=True)
    flat5 = models.FileField(upload_to='uploads/', validators=[validate_file_extension], null=True, blank=True)

    class Meta:
        verbose_name_plural = "SchoolMap"

    def __str__(self):
        return f'{self.school}'
