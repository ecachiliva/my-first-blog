from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicar



def inicio(request):
	posts = Publicar.objects.filter(data_publicar__lte=timezone.now()).order_by('data_publicar')
	return render(request, 'blog/index.html', {'posts': posts})

def publicar_list(request):
	posts = Publicar.objects.filter(data_publicar__lte=timezone.now()).order_by('data_publicar')
	return render(request, 'blog/publicar_list.html', {'posts': posts})

def publicar_detalle(request, pk):
	post = get_object_or_404(Publicar, pk=pk)
	return render(request, 'blog/publicar_detalle.html', {'post': post})

