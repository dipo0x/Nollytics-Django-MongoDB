from searches import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name='searches'

urlpatterns = [
    path('search/', views.search_view)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


