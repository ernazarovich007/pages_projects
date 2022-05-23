from django.urls import path
from .views import HomePageView, AboutPagevIEW, CallPageView

urlpatterns = [
    path('call/', CallPageView.as_view(), name='call'),
    path('about/', AboutPagevIEW.as_view(), name='about'),
    path('', HomePageView.as_view(),name='home'),
]




