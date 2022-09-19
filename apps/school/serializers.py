import uuid
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        school = validated_data['school']
        if school.students.count() >= school.max_students:
            raise ValidationError(detail=f'{school.name} already reached max students')
        return super(StudentSerializer, self).create(validated_data)
