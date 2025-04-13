from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('submit', views.submit),
    path('review', views.review),
    path('business/', include('BUSINESS.urls')),
]
