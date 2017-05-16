from django import template

register = template.Library()

from ..models import *


@register.inclusion_tag('app/latest_news.html')
def show_latest_news(count=5):
	latest_news = NewsEvent.objects.filter(category='News').order_by('-created')[:count]
	return {'latest_news': latest_news}


@register.inclusion_tag('app/latest_event.html')
def show_latest_event(count=5):
	latest_event = NewsEvent.objects.filter(category='Event').order_by('-created')[:count]
	return {'latest_event': latest_event}