from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('notes/', views.HomeView.as_view()),
    path('add-note/', views.CreateNoteView.as_view()),
    path('update/<int:pk>/', views.UpdateNoteView.as_view()),
    path('delete/<int:pk>/', views.DeleteNoteView.as_view()),
]
