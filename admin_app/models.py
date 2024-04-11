from django.db import models
from colorfield.fields import ColorField
from django.db.models.signals import pre_save
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import qrcode
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


class School(models.Model):
    school_kz_name = models.CharField('school_full_name', max_length=255)
    school_ru_name = models.CharField('school_full_name', max_length=255, null=True)
    school_eng_name = models.CharField('school_full_name', max_length=255, null=True)
    url = models.CharField('url', max_length=255)
    REGION_CHOICES = [
        ('almaty', 'almaty'),
        ('astana', 'astana'),
        ('shymkent', 'shymkent'),
        ('abay_oblast', 'abay_oblast'),
        ('akmolinsk_oblast', 'akmolinsk_oblast'),
        ('aktobe_oblast', 'aktobe_oblast'),
        ('almaty_region', 'almaty_region'),
        ('atyrau_oblast', 'atyrau_oblast'),
        ('east_kazakhstan_oblast', 'east_kazakhstan_oblast'),
        ('zhambyl_oblast', 'zhambyl_oblast'),
        ('zhetysu_oblast', 'zhetysu_oblast'),
        ('west_kazakhstan_oblast', 'west_kazakhstan_oblast'),
        ('karaganda_oblast', 'karaganda_oblast'),
        ('kostanay_oblast', 'kostanay_oblast'),
        ('kyzylorda_oblast', 'kyzylorda_oblast'),
        ('mangystau_oblast', 'mangystau_oblast'),
        ('pavlodar_oblast', 'pavlodar_oblast'),
        ('north_kazakhstan_oblast', 'north_kazakhstan_oblast'),
        ('turkestan_oblast', 'turkestan_oblast'),
        ('ulytau_oblast', 'ulytau_oblast'),
    ]
    region = models.CharField('region', max_length=255, choices=REGION_CHOICES, null=True,blank=True)
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
    user = models.OneToOneField('auth_user.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='school_user')

    class Meta:
        verbose_name_plural = 'Schools'

    def __str__(self):
        return f'{self.school_kz_name}'

class Classrooms(models.Model):
    classroom_name = models.CharField(max_length=250)
    classroom_number = models.IntegerField(default=1)
    flat = models.IntegerField()
    korpus = models.IntegerField()
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Classrooms'

    def __str__(self):
        return f'{self.classroom_name}'

class Teacher(models.Model):
    full_name = models.CharField(max_length=250)
    photo3x4 = models.ImageField(null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=250, null=True,blank=True)
    PEDAGOG_CHOICES = [
        ('pedagog_sheber', 'pedagog_sheber'),
        ('pedagog_zertteushy', 'pedagog_zertteushy'),
        ('pedagog_sarapshy', 'pedagog_sarapshy'),
        ('pedagog_moderator', 'pedagog_moderator'),
        ('pedagog', 'pedagog'),
        ('pedagog_stazher', 'pedagog_stazher'),
        ('pedagog_zhogary', 'pedagog_zhogary'),
        ('pedagog1sanat', 'pedagog1sanat'),
        ('pedagog2sanat', 'pedagog2sanat'),
        ('pedagog_sanat_zhok', 'pedagog_sanat_zhok'),
    ]
    pedagog = models.CharField(
        max_length=200,
        choices=PEDAGOG_CHOICES,
        null=True, blank=True,
        default='pedagog'
    )
    class Meta:
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f'{self.full_name}'

class Class(models.Model):
    class_name = models.CharField(max_length=150)
    class_number = models.CharField(max_length=255, editable=False, null=True, blank=True)
    class_letter = models.CharField(max_length=1, null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True,blank=True)
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
        null=True, blank=True
    )
    osnova_plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)],null=True)
    osnova_smena = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 5)],null=True)
    dopurok_plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)],null=True)
    dopurok_smena = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 5)],null=True)

    def save(self, *args, **kwargs):
        if self.class_name:
            numbers = [int(s) for s in self.class_name if s.isdigit()]
            letters = [s.upper() for s in self.class_name if s.isalpha()]  # Преобразуем буквы в верхний регистр
            self.class_number = ''.join(map(str, numbers))
            self.class_letter = ''.join(letters)
            self.class_name = self.class_name.strip()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f'{self.class_name} {self.school}'

class TeacherWorkload(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    classl = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 51)])
    classroom = models.ForeignKey('Classrooms', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.teacher} Workload"



class Ring(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 10)])
    smena = models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'),(3, '3 смена'),(4, '4 смена')], default=1)
    number = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)])
    start_time = models.TimeField(default=datetime.time(0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0))
    def __str__(self):
        return f'{self.start_time}-{self.end_time}'

class DopUrokRing(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 10)])
    smena = models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'),(3, '3 смена'),(4, '4 смена')], default=1)
    number = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 20)])
    start_time = models.TimeField(default=datetime.time(0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0))
    def __str__(self):
        return f'{self.start_time}-{self.end_time}'


class Schedule(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
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
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    classl = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    ring = models.ForeignKey('Ring', on_delete=models.SET_NULL,null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.SET_NULL, null=True,blank=True)
    teacher2 = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True,blank=True, related_name='teacher_g2')
    classroom2 = models.ForeignKey('Classrooms', on_delete=models.SET_NULL, null=True,blank=True, related_name='classroom_g2')
    subject2 = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, blank=True, related_name='subject_g2')
    typez = models.ForeignKey('Extra_Lessons', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return f'{self.school} {self.classl} - {self.week_day}'

class DopUrok(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
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
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    classl = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    ring = models.ForeignKey('DopUrokRing', on_delete=models.SET_NULL,null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.SET_NULL, null=True)
    teacher2 = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True,blank=True, related_name='teacher2')
    classroom2 = models.ForeignKey('Classrooms', on_delete=models.SET_NULL, null=True,blank=True, related_name='classroom2')
    subject2 = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, blank=True, related_name='subject2')
    typez = models.ForeignKey('Extra_Lessons', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return f'{self.school} {self.classl} - {self.week_day}'



class Menu(models.Model):
    food_name = models.CharField(max_length=250)
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
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null = True)

    class Meta:
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.food_name}'

class Slider(models.Model):
    slider_name = models.CharField(max_length=355)
    slider_photo = models.ImageField(null=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)

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
    date = models.DateField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, related_name='news')
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default=MANUAL,
    )
    img1 = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)
    img5 = models.ImageField(null=True, blank=True)
    img6 = models.ImageField(null=True, blank=True)
    img7 = models.ImageField(null=True, blank=True)
    img8 = models.ImageField(null=True, blank=True)
    img9 = models.ImageField(null=True, blank=True)
    img10 = models.ImageField(null=True, blank=True)
    qr_code = models.ImageField(blank=True, null=True, upload_to='news_qrcodes/')

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.date} {self.type} {self.school} news'

    def save(self, *args, **kwargs):
        if self.type == 'facebook':
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer)
            filename = f'qr_code_{self.id}.png'

            # Удаляем старый QR-код перед сохранением нового
            if self.qr_code:
                self.qr_code.delete()

            self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)

# Сигнал для удаления QR-кода при удалении новости
from django.db.models.signals import pre_delete
from django.dispatch import receiver
@receiver(pre_delete, sender=News)
def delete_qr_code(sender, instance, **kwargs):
    # Удаляем QR-код при удалении новости
    if instance.qr_code:
        instance.qr_code.delete(False)  # Удаляем файл из хранилища



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
        choices=type_choices,null=True,blank=True
    )
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f'{self.full_name}'



# =============== School Pasport ============================================================

class schoolPasport(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    school_name = models.CharField(max_length=355, null=True,blank=True)
    photo = models.ImageField()
    established = models.IntegerField(default=2008,null=True,blank=True)
    school_address = models.CharField(max_length=250,null=True,blank=True)
    amount_of_children = models.IntegerField(null=True,blank=True)
    ul_sany = models.IntegerField(null=True,blank=True)
    kiz_sany = models.IntegerField(null=True,blank=True)
    school_lang = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=250,null=True,blank=True)
    vmestimost = models.IntegerField(null=True,blank=True)
    dayarlyk_class_number = models.IntegerField(null=True,blank=True)
    dayarlyk_student_number = models.IntegerField(null=True,blank=True)
    number_of_students = models.IntegerField(null=True,blank=True)
    number_of_classes = models.IntegerField(null=True,blank=True)
    number_of_1_4_students = models.IntegerField(null=True,blank=True)
    number_of_1_4_classes = models.IntegerField(null=True,blank=True)
    number_of_5_9_students = models.IntegerField(null=True,blank=True)
    number_of_5_9_classes = models.IntegerField(null=True,blank=True)
    number_of_10_11_students = models.IntegerField(null=True,blank=True)
    number_of_10_11_classes = models.IntegerField(null=True,blank=True)
    amount_of_family = models.IntegerField(null=True,blank=True)
    amount_of_parents = models.IntegerField(null=True,blank=True)
    all_pedagog_number = models.IntegerField(null=True,blank=True)
    pedagog_sheber = models.IntegerField(null=True,blank=True)
    pedagog_zertteushy = models.IntegerField(null=True,blank=True)
    pedagog_sarapshy = models.IntegerField(null=True,blank=True)
    pedagog_moderator = models.IntegerField(null=True,blank=True)
    pedagog = models.IntegerField(null=True,blank=True)
    pedagog_stazher = models.IntegerField(null=True,blank=True)
    pedagog_zhogary = models.IntegerField(null=True,blank=True)
    pedagog_1sanat = models.IntegerField(null=True,blank=True)
    pedagog_2sanat = models.IntegerField(null=True,blank=True)
    pedagog_sanat_zhok = models.IntegerField(null=True,blank=True)
    school_history = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'School Pasport'

    def __str__(self):
        return f'{self.school} + School Passport'


class School_SocialMedia(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    YOUTUBE = 'youtube'
    WEBSITE = 'website'
    TGBOT = 'tgbot'
    SOCIAL_MEDIA_CHOICES = [
        (INSTAGRAM, 'instagram'),
        (FACEBOOK, 'facebook'),
        (YOUTUBE, 'youtube'),
        (WEBSITE, 'website'),
        (TGBOT, 'tgbot')
    ]
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default=YOUTUBE,
    )
    account_name = models.CharField(max_length=250,null=True,blank=True)
    qr_code = models.ImageField(blank=True, null=True, upload_to='social_media_qrcodes/')

    class Meta:
        verbose_name_plural = "School Social Media"
        unique_together = ['school', 'type']

    def __str__(self):
        return f'{self.school} Social Media {self.type}'

@receiver(pre_save, sender=School_SocialMedia)
def generate_or_update_qr_code(sender, instance, **kwargs):
    # Генерируем или обновляем QR-код и сохраняем его в поле qr_code
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Используем URL социальной медиа при создании QR-кода
    url = instance.account_name
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer)
    filename = f'qr_code.png'

    # Если у объекта уже есть QR-код, удалим его перед сохранением нового
    if instance.qr_code:
        instance.qr_code.delete(False)

    instance.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

@receiver(pre_delete, sender=School_SocialMedia)
def delete_qr_code(sender, instance, **kwargs):
    # Удаляем QR-код при удалении социальной медиа
    if instance.qr_code:
        instance.qr_code.delete(False)

class School_Administration(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    administrator_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    administator_photo = models.ImageField(null=True,blank=True)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "School Administration"

    def __str__(self):
        return f'{self.school} - {self.administrator_name}'


# =================== Pride_of_the_School =====================================================

class Sport_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=150,null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)
    student_success = models.TextField(null=True,blank=True)
    classl = models.CharField(max_length=100, null=True,blank=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Sport"

    def __str__(self):
        return f'{self.fullname}'

class Oner_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True,blank=True)
    fullname = models.CharField(max_length=150,null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)
    student_success = models.TextField(null=True,blank=True)
    classl = models.CharField(max_length=100, null=True,blank=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Oner"

    def __str__(self):
        return f'{self.fullname}'

class PandikOlimpiada_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=150,null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)
    student_success = models.TextField(null=True,blank=True)
    classl = models.CharField(max_length=100, null=True,blank=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Olimpiada"

    def __str__(self):
        return f'{self.fullname}'

class RedCertificate(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(null=True)
    student_success = models.CharField(max_length=250)
    endyear = models.CharField(max_length=10, default="2011-2022")

    class Meta:
        verbose_name_plural = "Red Certificate"

    def __str__(self):
        return f'{self.fullname}, {self.school}, {self.endyear}'

class AltynBelgi(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(null=True)
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
    director_photo = models.ImageField(null=True)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "School Director"

    def __str__(self):
        return f'{self.director_name}'

class Extra_Lessons(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
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
    start_date = models.CharField(max_length=100,null=True,blank=True)
    end_date = models.CharField(max_length=4,null=True,blank=True)
    job_characteristic = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Job History"

    def __str__(self):
        return f'{self.teacher} History'


class SpecialityHistory(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=False)
    end_date = models.CharField(max_length=100,null=True,blank=True)
    speciality_university = models.TextField(null=True,blank=True)
    mamandygy = models.CharField(max_length=150, null=True,blank=True)
    DEGREE_CHOICES = [
        ('bakalavr', 'bakalavr'),
        ('magistratura', 'magistratura'),
        ('doktorantura', 'doktorantura'),
        ('srednee', 'srednee'),
        ('viswee', 'viswee'),
    ]
    degree = models.CharField(
        max_length=200,
        choices=DEGREE_CHOICES,
        default='bakalavr',null=True,blank=True
    )

    class Meta:
        verbose_name_plural = "Speciality History"

    def __str__(self):
        return f'{self.teacher} Speciality History'


    # ======================================================================================

class Kruzhok(models.Model):
    kruzhok_name = models.CharField(max_length=250,null=True,blank=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,blank=True)
    photo = models.ImageField(upload_to='main/static/img',null=True)
    purpose = models.CharField(max_length=500,null=True,blank=True)
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
    kruzhok = models.ForeignKey(Kruzhok, on_delete=models.CASCADE, related_name='lessons',null=True,blank=True)
    week_day = models.CharField(
        max_length=20,
        choices=Kruzhok.WEEK_DAY_CHOICES,
        default=Kruzhok.Monday,null=True,blank=True
    )
    start_end_time = models.CharField(max_length=150,blank=True,null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return f'{self.kruzhok.kruzhok_name} - {self.week_day} {self.start_end_time}'

class Notifications(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f'{self.school} + {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'

class SchoolMap(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    map = models.FileField(upload_to='uploads/',null=True, blank=True)
    flat1 = models.FileField(upload_to='uploads/',null=True, blank=True)
    flat2 = models.FileField(upload_to='uploads/', null=True, blank=True)
    flat3 = models.FileField(upload_to='uploads/', null=True, blank=True)
    flat4 = models.FileField(upload_to='uploads/', null=True, blank=True)
    flat5 = models.FileField(upload_to='uploads/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "SchoolMap"

    def __str__(self):
        return f'{self.school}'
    
class MainSchoolPhoto(models.Model):
    photo1 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo2 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo3 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo4 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo5 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo6 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo7 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo8 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo9 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    photo10 = models.ImageField(upload_to='school_photos/',null=True,blank=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, related_name='school')

    class Meta:
        verbose_name_plural = "MainSchoolPhoto"

    def __str__(self):
        return f'{self.school}'

class MapCoordinates(models.Model):
    x = models.CharField(max_length=255)
    y = models.CharField(max_length=255)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, related_name='school_coordinates')

    class Meta:
        verbose_name_plural = "MapCoordinates"

    def __str__(self):
        return f'{self.x}_{self.y}_{self.school}'