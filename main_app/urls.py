from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vids/', views.vids_index, name='index'),
    path('vids/<int:vid_id>/', views.vids_detail, name='detail'),
    path('vids/create/', views.VidCreate.as_view(), name='vids_create'),
    path('vids/<int:pk>/update/', views.VidUpdate.as_view(), name='vids_update'),
    path('vids/<int:pk>/delete/', views.VidDelete.as_view(), name='vids_delete'),
    path('vids/<int:vid_id>/add_progress/', views.add_progress, name='add_progress'),
    path('vids/<int:vid_id>/assoc_character/<int:character_id>/', views.assoc_character, name='assoc_character'),
    path('vids/<int:cat_id>/unassoc_character/<int:character_id>/', views.unassoc_character, name='unassoc_character'),
    # path('toys/', views.ToyList.as_view(), name='toys_index'),
    # path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
]
