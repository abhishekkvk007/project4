from django.urls import path
from .views import RegView,LogView,HomeView

urlpatterns=[
    path('reg/',RegView.as_view(),name="reg"),
    path('login/',LogView.as_view(),name="log"),
    path('mhome',HomeView.as_view(),name="h"),
    path('logout',LogView.as_view(),name="logout"),
   


]