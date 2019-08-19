from django.conf.urls.static import static
from django.urls import path, include
from sky_code import settings
from skycode import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teachers', views.TeacherView)
router.register('courses', views.CourseView)


urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.get_courses, name='courses'),
    path('ask/', views.ask_question, name='question'),
    path('enroll/', views.enroll_course, name='enroll'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
