from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


from .models import Author, Genre, Book, BookInstance, Language
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BooksInline(admin.TabularInline):
    model = Book


# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'
    inlines = [BooksInstanceInline]


# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
<<<<<<< HEAD
=======
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
>>>>>>> Django Tutorial Part 4: Django admin site
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
<<<<<<< HEAD
=======
    list_display = ('title', 'author', 'display_genre')
>>>>>>> Django Tutorial Part 4: Django admin site
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre) # Genre register
<<<<<<< HEAD
admin.site.register(Language) # Language register
=======
admin.site.register(Language) # Language register
>>>>>>> Django Tutorial Part 4: Django admin site
