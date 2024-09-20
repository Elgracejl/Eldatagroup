from django.contrib import admin
from .models import *

# Register your models here.

class blogAdmin(admin.ModelAdmin):
    list_display = ('titre', 'framework') #tableau
    list_filter = ('titre', 'framework') #classe par odre des taches terminés
    search_fields = ('titre', 'framework')
admin.site.register(Blog, blogAdmin)

class portfolioAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description') #tableau
    list_filter = ('titre', 'description') #classe par odre des taches terminés
    search_fields = ('titre', 'description')
admin.site.register(My_portfolio, portfolioAdmin)

admin.site.register(Category)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'sujet', 'message')