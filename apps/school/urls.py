from django.urls import path
from rest_framework_nested import routers
# from rest_framework import routers

from .views import SchoolViewSet, StudentViewSet


router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)

school_router = routers.NestedSimpleRouter(
    router,
    r'schools',
    lookup='school',
)

school_router.register(
    r'students',
    StudentViewSet,
    basename='school-student'
)

app_name = 'school'

urlpatterns = router.urls + school_router.urls
