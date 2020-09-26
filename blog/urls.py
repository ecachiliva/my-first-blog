from django.urls import path
from .views import publicar_list
urlpatterns = [

	#path('', inicio, name="inicio"),
	path('', publicar_list, name="publicar_list"),
]