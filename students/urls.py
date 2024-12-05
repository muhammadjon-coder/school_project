from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    path('create/', views.student_form, name='create'),
    path('detail/<int:pk>/', views.student_detail, name='detail'),
    path('delete/<int:pk>/', views.student_delete, name='delete')
]
