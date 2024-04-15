from django.urls import path
from . import views

urlpatterns = [
    path('mars_photos', views.MarsPhotosGenericAPIView.as_view(), name='mars_photos'),
]