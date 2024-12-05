from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.groups_list, name='group_list'),
    path('create/', views.group_form, name='create'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
    path('delete/<int:pk>/', views.group_delete, name='delete')
]
