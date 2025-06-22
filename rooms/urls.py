from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room-list'),
    path('rooms/<int:id>/', views.room_detail, name='room-detail'),
    path('rooms/add/', views.add_room, name='add-room'),  # Added POST route for adding room
]
