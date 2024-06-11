from rest_framework import serializers
from admin_app.models import *
from .models import *


class ClassGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = '__all__'

class GeneratedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedSchedule
        fields = '__all__'
        depth = 1

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class GenerateScheduleRequestSerializer(serializers.Serializer):
    school_id = serializers.IntegerField()