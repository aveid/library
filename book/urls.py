from django.urls import path
from . import views
urlpatterns = [
    path("books/", views.BookAPIView.as_view()),
    path("books/<int:pk>/", views.BookDetailUpdateDeleteAPIView.as_view()),
]