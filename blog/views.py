from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicar
from .forms import PublicarForm



def inicio(request):
	posts = Publicar.objects.filter(data_publicar__lte=timezone.now()).order_by('data_publicar')
	return render(request, 'blog/index.html', {'posts': posts})

# def publicar_crear(request):
# 	form = PublicarForm()
# 	return render(request, 'blog/publicar_edit.html',{'form': form})
def publicar_crear(request):
	if request.method == "POST":
		form = PublicarForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.save()
			return redirect('blog/publicar_detalle.html', pk=post.pk)
	else:
		form = PublicarForm()
		return render(request, 'blog/publicar_edit.html', {'form': form})

def publicar_list(request):
	posts = Publicar.objects.filter(data_publicar__lte=timezone.now()).order_by('data_publicar')
	return render(request, 'blog/publicar_list.html', {'posts': posts})

def publicar_detalle(request, pk):
	post = get_object_or_404(Publicar, pk=pk)
	return render(request, 'blog/publicar_detalle.html', {'post': post})

def publicar_editar(request, pk):
	post = get_object_or_404(Publicar, pk=pk)
	if request.method == "POST":
		form = PublicarForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.save()
			return redirect('publicar_detalle', pk=post.pk)
	else:
		form = PublicarForm(instance=post)
	return render(request, 'blog/publicar_edit.html', {'form': form})

