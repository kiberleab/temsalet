from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')
	list_filter = ('created',)

admin.site.register(Category, CategoryAdmin)

class MenuAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'price', 'created')
	list_filter = ('category',)

admin.site.register(Menu, MenuAdmin)

class NewsEventAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'created')
	list_filter = ('category', 'created')

admin.site.register(NewsEvent, NewsEventAdmin)