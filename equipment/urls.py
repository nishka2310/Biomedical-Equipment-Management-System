from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.equipment_list,
        name='equipment_list'
    ),

    path(
        'add/',
        views.add_equipment,
        name='add'
    ),

    path(
        'edit/<int:id>/',
        views.edit_equipment,
        name='edit'
    ),

    path(
        'delete/<int:id>/',
        views.delete_equipment,
        name='delete'
    ),
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


]

path(
'dashboard/',
views.dashboard,
name='dashboard'
)