from django.urls import path
from . import views

urlpatterns = [
    path('add_lashes/<int:id>', views.add_lashes, name='add_lashes'),
    path('subtract_lashes/<int:id>', views.subtract_lashes, name='subtract_lashes'),
    path('create/', views.create_lashes, name='create_lashes'),
    path('update/<int:lashes_id>/', views.update_lashes, name='update_lashes'),
    path('delete/<int:lashes_id>/', views.delete_lashes, name='delete_lashes'),
    path('lasheslist/', views.get_lashes, name='get_lashes'),
]
