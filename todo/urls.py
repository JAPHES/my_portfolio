from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success, name='success'),
    #path('gallery/', views.gallery, name='gallery'),  # Gallery page
    path('cv/', views.cv_page, name='cv_page'),

]


