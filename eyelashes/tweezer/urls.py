from django.urls import path
from . import views

urlpatterns = [
    path('add_tweezer/<int:id>', views.add_tweezer, name='add_tweezer'),
    path('subtract_tweezer/<int:id>', views.subtract_tweezer, name='subtract_tweezer'),
    path('create/', views.create_tweezer, name='create_tweezer'),
    path('update/<int:tweezer_id>/', views.update_tweezer, name='update_tweezer'),
    path('delete/<int:tweezer_id>/', views.delete_tweezer, name='delete_tweezer'),
     path('tweezerlist/', views.get_tweezers, name='get_tweezers'),
]
