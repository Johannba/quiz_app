from django.urls import path
from . import views

urlpatterns = [
    path('carousel/', views.carousel, name='carousel'),
    path('carousel/upload/', views.upload_image, name='upload_image'),
]
