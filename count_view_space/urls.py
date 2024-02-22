from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookCountView.as_view(), name='count_books'),
    path('user', views.UserVisitsCountView.as_view(), name='count_user_visits'),
]