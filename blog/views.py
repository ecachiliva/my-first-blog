from django.shortcuts import render
from django.utils import timezone
from .models import Publicar

def publicar_list(request):
	posts = Publicar.objects.filter(data_publicar__lte=timezone.now()).order_by('data_publicar')
	return render(request, 'blog/publicar_list.html', {'posts': posts})
