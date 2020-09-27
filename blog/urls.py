from django.urls import path
from .views import publicar_list, inicio, publicar_detalle, publicar_crear, publicar_editar
urlpatterns = [

	# path('', inicio, name="inicio"),
	path('', publicar_list, name="publicar_list"),
	path('adicionar/', publicar_crear, name='publicar_crear'),
	path('<int:pk>/detalle/', publicar_detalle, name='publicar_detalle'),
	path('<int:pk>/editar/', publicar_editar, name='publicar_editar'),
]