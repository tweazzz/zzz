from django.contrib import admin
from admin_app.models import *
from django.forms import modelformset_factory, ClearableFileInput, HiddenInput
from django import forms
from auth_user.models import User



admin.site.register(Nationality)
admin.site.register(Classroom)

class JobHistoryInline(admin.TabularInline):
    model = JobHistory
    extra = 1

class SpecialityHistoryInline(admin.TabularInline):
    model = SpecialityHistory
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    inlines = [JobHistoryInline, SpecialityHistoryInline]
admin.site.register(Teacher,TeacherAdmin)


from django.contrib.auth.admin import UserAdmin

class UsersAdmin(UserAdmin):
    list_display = ('username', 'email','role','is_superuser')
    list_display_links = ('username',)
    search_fields = ('email', 'username', )
    readonly_fields = ('id', )
    ordering = ('id',)
    filter_horizontal = ()
    list_filter = ('is_active', 'is_superuser')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2'),
        }),
    )
    list_filter = ('role',)

admin.site.register(User, UsersAdmin)

class PhotoforNewsInlineForm(forms.ModelForm):
    class Meta:
        model = PhotoforNews
        fields = '__all__'

class PhotoforNewsInline(admin.TabularInline):
    model = PhotoforNews
    form = PhotoforNewsInlineForm
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [PhotoforNewsInline]

admin.site.register(News, NewsAdmin)



admin.site.register(Menu)
admin.site.register(Slider)
admin.site.register(schoolPasport)
admin.site.register(School_Administration)
admin.site.register(School_Director)
admin.site.register(Extra_Lessons)
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class KruzhokAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

admin.site.register(Kruzhok, KruzhokAdmin)

admin.site.register(DopUrok)
admin.site.register(TeacherWorkload)
admin.site.register(Sport_Success)
admin.site.register(Oner_Success)
admin.site.register(PandikOlimpiada_Success)
admin.site.register(RedCertificate)
admin.site.register(AltynBelgi)
admin.site.register(School_SocialMedia)
admin.site.register(DopUrokRing)
admin.site.register(Notifications)

admin.site.register(School)
admin.site.register(Subject)
admin.site.register(ClassGroup)
admin.site.register(TeacherSubject)
admin.site.register(Schedule)
admin.site.register(Ring)
admin.site.register(SchoolMap)
admin.site.register(SchoolLessonTime)
admin.site.register(MainSchoolPhoto)
admin.site.register(MapCoordinates)
