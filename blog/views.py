from django.shortcuts import render

def publicar_list(request):
	return render(request, 'blog/publicar_list.html')
