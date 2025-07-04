from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_event, name='register_event'),
    path('my/registrations/', views.my_registrations, name='my_registrations'),
    path('logout/', views.custom_logout, name='logout'),  # 👈 Add this line
]
