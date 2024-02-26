from django.urls import path
from . import views

urlpatterns = [
    path('add_glue/<int:id>', views.add_glue, name='add_glue'),
    path('subtract_glue/<int:id>', views.subtract_glue, name='subtract_glue'),
    path('create/', views.create_glue, name='create_glue'),
    path('update/<int:glue_id>/', views.update_glue, name='update_glue'),
    path('delete/<int:glue_id>/', views.delete_glue, name='delete_glue'),
     path('gluelist/', views.get_glues, name='get_glues'),
]
