from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='MainPage.html'),
    path('HomePage.html',
         views.home, name='HomePage.html'),
    path('Add_New_Student_Page.html',
         views.Add, name='Add_New_Student_Page.html'),
    path('Activitystatus.html',
         views.activity, name='Activitystatus.html'),
    path('SearchInfo_Table.html',
         views.search, name='SearchInfo_Table.html'),
    path('UpdateDelete.html',
         views.update, name='UpdateDelete.html'),
    path('student_assignment.html',
         views.assign, name='student_assignment.html'),
]
