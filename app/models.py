from django.db import models
from django.utils import timezone


class Category(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('title',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.title


class Menu(models.Model):
	title = models.CharField(max_length=250)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menus')
	price = models.DecimalField(max_digits=9, decimal_places=2)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('title',)
		verbose_name = 'menu'
		verbose_name_plural = 'menus'

	def __str__(self):
		return self.title


class NewsEvent(models.Model):
	CHOICE = (('Event', 'Event'), ('News', 'News'))

	title = models.CharField(max_length=250)
	sub_title = models.CharField(max_length=250, blank=True)
	detail = models.TextField()
	image = models.ImageField(upload_to='app/%Y/%m/%d')
	category = models.CharField(max_length=6, choices=CHOICE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)
		verbose_name = 'newsevent'
		verbose_name_plural = 'newsevents'

	def __str__(self):
		return self.title
