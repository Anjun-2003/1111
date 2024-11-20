from django.contrib import admin
from .models import Book,Review
# Register your models here.
# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ("id",'title', 'description')
    list_display = ['title', 'description']
    list_editable = ('description',)
    
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
