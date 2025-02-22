from django.urls import path
from . import views
from .views import upload_project, project_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'home'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success, name='success'),
    path('cv/', views.cv_page, name='cv_page'),
    path('upload/', upload_project, name='upload_projects'),
    path('project_list/', project_list, name='project_list'),
    path('gallery/', views.gallery, name='gallery'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
