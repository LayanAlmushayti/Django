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
    path('search/', views.search_books, name='book_search'),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='book_search'),
    path('lab8/task1/', views.list_books_task1, name='list_books_task2'),
    path('lab8/task2/', views.list_books_task2, name='list_books_task2'),
    path('lab8/task3/', views.list_books_task3, name='list_books_task3'),
    path('lab8/task4/', views.list_books_task4, name='list_books_ordered_by_title'),
    path('lab8/task5/', views.books_aggregates, name='books_aggregates'),
    path('students-per-city/', views.students_per_city, name='students_per_city'),
    path('lab9/task1/', views.department_student_count, name='department_student_count'),
    path('lab9/task2/', views.course_student_count, name='course_student_count'),
    path('lab9/task3/', views.oldest_student_per_department, name='oldest_student_per_department'),
    path('lab9/task4/', views.departments_with_more_than_two_students, name='departments_with_more_than_two_students'),
    path('lab9_part1/listbooks/', views.list_books, name='list_books'),
    path('lab9_part1/addbook/', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),

    path('lab9_part2/listbooks/', views.list_books_form, name='list_books_form'),
    path('lab9_part2/addbook/', views.add_book_form, name='add_book_form'),
    path('lab9_part2/editbook/<int:id>/', views.edit_book_form, name='edit_book_form'),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book_form, name='delete_book_form'),




]


