from rest_framework import serializers
from admin_app.models import Teacher, Class, Subject
from autogenerate.utils import BaseSerializer

class AutoScheduleSerializer(BaseSerializer):
    teacher = serializers.PrimaryKeyRelatedField(many=False, queryset=Teacher.objects.all())
    school_class = serializers.PrimaryKeyRelatedField(many=False, queryset=Class.objects.all())
    subject = serializers.PrimaryKeyRelatedField(many=False, queryset=Subject.objects.all())
    lessons_per_week = serializers.IntegerField()
    subgroup = serializers.BooleanField()
    double_lesson = serializers.BooleanField(default=False)
    total_load = serializers.IntegerField()
