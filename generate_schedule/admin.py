from django.contrib import admin
from .models import GeneratedSchedule


# Register your models here.
class GeneratedScheduleAdmin(admin.ModelAdmin):
    list_display = ('school', 'class_group', 'subject', 'teacher', 'ring', 'classroom', 'week_day', 'shift', 'start_time', 'end_time')
    list_filter = ('school', 'class_group', 'teacher', 'week_day', 'shift')
    search_fields = ('school__school_kz_name', 'class_group__class_name', 'subject__full_name', 'teacher__full_name', 'classroom__classroom_name')
    ordering = ('school', 'class_group', 'week_day', 'ring__start_time')
    actions = ['export_as_csv']

    def start_time(self, obj):
        return obj.ring.start_time if obj.ring else None

    def end_time(self, obj):
        return obj.ring.end_time if obj.ring else None

    start_time.short_description = 'Start Time'
    end_time.short_description = 'End Time'

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=generated_schedule.csv'
        writer = csv.writer(response)

        writer.writerow(['School', 'Class Group', 'Subject', 'Teacher', 'Ring', 'Classroom', 'Week Day', 'Shift', 'Start Time', 'End Time'])
        for schedule in queryset:
            writer.writerow([
                schedule.school,
                schedule.class_group,
                schedule.subject,
                schedule.teacher,
                schedule.ring,
                schedule.classroom,
                schedule.week_day,
                schedule.shift,
                schedule.start_time(),
                schedule.end_time()
            ])

        return response

    export_as_csv.short_description = "Export Selected as CSV"

admin.site.register(GeneratedSchedule, GeneratedScheduleAdmin)