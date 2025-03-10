from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('links/', views.links, name='/books.html5/links'),
    path('text/formatting', views.textformat, name='/books.html5/textformatting'),
    path('listing/', views.listing, name='/books.html5/listing'),
    path('tables/', views.tables, name='/books.html5/tables'),
]


