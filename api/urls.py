from . import views
from django.urls import path



urlpatterns = [
    path('notes/', views.HomeView.as_view()),
    path('add-note/',views.CreateNoteView.as_view()),
    path('update/<int:pk>/', views.UpdateNoteView.as_view()),
    path('delete/<int:pk>/', views.DeleteNoteView.as_view()),
]