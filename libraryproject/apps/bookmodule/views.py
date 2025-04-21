from django.shortcuts import render 
from .models import Book

from django.http import HttpResponse

from django.db.models import Q ,Count, Sum, Avg, Max, Min , OuterRef, Subquery

from .models import Student , Department , Course , Student2


# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html" , {"name": name})  #your render line


def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))



def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def textformat(request):
    return render(request, 'bookmodule/textformat.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Get books list
        books = __getBooksList()
        filtered_books = []

        for book in books:
            found = False
            if isTitle and string in book['title'].lower():
                found = True
            if not found and isAuthor and string in book['author'].lower():
                found = True

            if found:
                filtered_books.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

    return render(request, "bookmodule/search_page.html")  # Load the form if GET request



def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})



def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 50)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


#######################################################################################

def list_books_task1(request):
    books = Book.objects.filter(Q(price__lte=20))
    return render(request, 'bookmodule/task1.html', {'books': books})


def list_books_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})


def list_books_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        (~Q(title__icontains='co') & ~Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})


def list_books_task4(request):
    books = Book.objects.order_by('title')  
    return render(request, 'bookmodule/task4.html', {'books': books})
 
def books_aggregates(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})




def students_per_city(request):
    data = Student.objects.values('address__city').annotate(total=Count('id')).order_by('address__city')
    return render(request, 'bookmodule/students_per_city.html', {'data': data})



#lab 9

def department_student_count(request):
    data = Department.objects.annotate(total_students=Count('student2'))
    return render(request, 'bookmodule/lab9_task1.html', {'data': data})

def course_student_count(request):
    data = Course.objects.annotate(total_students=Count('student2'))
    return render(request, 'bookmodule/lab9_task2.html', {'data': data})


def oldest_student_per_department(request):
    # Subquery to find the oldest student (by ID) in each department
    oldest_students = Student2.objects.filter(
        department=OuterRef('pk')
    ).order_by('id')  # oldest = smallest ID

    data = Department.objects.annotate(
        oldest_student_name=Subquery(oldest_students.values('name')[:1]),
        oldest_student_age=Subquery(oldest_students.values('age')[:1])
    )

    return render(request, 'bookmodule/lab9_task3.html', {'data': data})


def departments_with_more_than_two_students(request):
    data = Department.objects.annotate(
        student_count=Count('student2')
    ).filter(student_count__gt=2).order_by('-student_count')

    return render(request, 'bookmodule/lab9_task4.html', {'data': data})
 

