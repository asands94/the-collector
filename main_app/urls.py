from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('books/<int:book_id>/add-note/', views.add_note, name='add-note'),
    path('books/<int:book_id>/add-rating/', views.add_rating, name='add-rating'),
]