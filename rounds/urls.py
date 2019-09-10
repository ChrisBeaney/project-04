from django.urls import path
from .views import CourseListView, CourseDetailView, ScoreListView, ScoreDetailView, ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view()),
    path('scores/', ScoreListView.as_view()),
    path('scores/<int:pk>/', ScoreDetailView.as_view()),
]
