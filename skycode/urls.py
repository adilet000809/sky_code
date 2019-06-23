from django.conf.urls.static import static
from django.urls import path
from sky_code import settings
from skycode import views


urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
