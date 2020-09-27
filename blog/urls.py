from django.urls import path
from .views import publicar_list, inicio, publicar_detalle
urlpatterns = [

	# path('', inicio, name="inicio"),
	path('', publicar_list, name="publicar_list"),
	#path('<int:pk>/', publicar_detalle, name="publicar_detalle"),
	path('<int:pk>/editar/', publicar_detalle, name='publicar_detalle'),
]