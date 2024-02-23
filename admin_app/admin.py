from django.contrib import admin
from admin_app.models import *
from django.forms import modelformset_factory, ClearableFileInput, HiddenInput
from django import forms
from auth_user.models import User




class JobHistoryInline(admin.TabularInline):
    model = JobHistory
    extra = 1

class SpecialityHistoryInline(admin.TabularInline):
    model = SpecialityHistory
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    inlines = [JobHistoryInline, SpecialityHistoryInline]

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class)

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



admin.site.register(News)


admin.site.register(School)
admin.site.register(Classrooms)
admin.site.register(Schedule)
class RingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TimeField: {'widget': admin.widgets.AdminTimeWidget},
    }
admin.site.register(Menu)
admin.site.register(Slider)
admin.site.register(Subject)
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
admin.site.register(Ring)
admin.site.register(DopUrokRing)
admin.site.register(Notifications)
admin.site.register(SchoolMap)