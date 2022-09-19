from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_class = [AllowAny]
    queryset = School.objects.all()
    filterset_fields = ('name',)


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_class = [AllowAny]
    queryset = Student.objects.select_related('school')
    filterset_fields = ('first_name', 'last_name', 'school')

    def get_queryset(self):
        school_id = self.kwargs.get('school_pk')
        if school_id is None:
            return self.queryset
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            raise NotFound('A school with this ID does not exist')
        return self.queryset.filter(school=school)
