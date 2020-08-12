from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    
    def get_queryset(self):
        return Book.objects.filter(title__icontains='')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})
    


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.filter(first_name__icontains='')[:5] # Get 5 authors containing the words in ''
    template_name = 'authors/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author
    
    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'book': book})
        