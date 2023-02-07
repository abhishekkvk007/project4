from django.urls import path
from .views import AddMarkView,AddStudentMView,StudentListView,StudDeleteView,StudEditMView

urlpatterns=[
    path('addmark/',AddMarkView.as_view(),name="addmark"),
    path('addstu/',AddStudentMView.as_view(),name="addstu"),
    path('viewstudent/',StudentListView.as_view(),name="viewstudent"),   
    path('delstudent/<int:ssid>',StudDeleteView.as_view(),name="delstu"), 
    path('editstudent/<int:sid>',StudEditMView.as_view(),name="editstu"),
]