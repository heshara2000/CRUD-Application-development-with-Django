from django.urls import path
from . import views


app_name = 'profiles'


urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('edit/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile-edit'),
    path('delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]