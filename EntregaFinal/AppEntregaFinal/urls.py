from django.urls import path
from AppEntregaFinal import views

urlpatterns = [
path('', views.inicio, name='Inicio'),
path('clientes', views.clientes, name='Clientes'),
path('tiendas', views.tiendas, name='Tiendas'),
path('nosotros', views.nosotros, name='Nosotros'),
path('categorias', views.categorias, name='Categorias'),
path('busquedaCategoria',views.busquedaCategoria, name='BuscarCategoria'),    
path('buscar',views.buscar, name='Buscar'),    
 
    
    
    
]