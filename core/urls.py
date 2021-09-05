from core import views
from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileDetailView



app_name='core'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
	path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('search-profile/<username>/', ProfileDetailView.as_view(), name='detail'),

    path('accounts/profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    #path('login/', LoginView.as_view(), name='login'),
    path('search_newco/', views.search_newco, name='search_newco'),
    path('search/', views.results, name='results'),
    path('profile/notifications', views.notifications, name='notifications'),
    path('search-profile/', views.search_profile, name='search-profile'),
    path('profile/create/', views.profile_create_view, name='create'),
    path('profile/update/', views.profile_update, name='update'),
    path('journal/', views.journal_list_view, name='journal-list'),
    path('journal/<str:slug>/', views.journal_detail_view, name='journal-detail'),
    path('add_post/', views.journal_create_view),
    path('journal/<str:slug>/delete', views.journal_delete_view, name='journal-delete'),
    path('journal/<str:slug>/edit', views.journal_update_view, name='journal-update'),
    path('journal/<id>/comment-delete', views.comment_delete_view, name='comment-delete'),


    
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
