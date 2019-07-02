from django.conf.urls.static import static
from django.urls import path
from sky_code import settings
from skycode import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.get_courses, name='courses'),
    path('ask/', views.ask_question, name='question'),
    path('enroll/', views.enroll_course, name='enroll'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
