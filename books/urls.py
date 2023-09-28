from django.urls import path
from . import views

urlpatterns = [
    # path('books/', views.getAllBooks, name='books')
    path("books/", views.BooksView.as_view())
]