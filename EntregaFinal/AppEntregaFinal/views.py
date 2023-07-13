from django.http import HttpResponse
from django.shortcuts import render
from AppEntregaFinal.models import Cliente, Categoria, Tienda
from AppEntregaFinal.forms import ClienteFormulario, TiendaFormulario, CategoriaFormulario  

# Create your views here.

def inicio(request):
    return render(request, 'AppEntregaFinal/inicio.html')

def tiendas(request):
    if request.method == "POST":
        miFormulario = TiendaFormulario(request.POST) #donde llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid: #Si pasó la validacion de django
            informacion = miFormulario.cleaned_data
            
            tienda = Tienda(nombre=informacion['nombre'], direccion=informacion['direccion'], telefono=informacion['telefono']) 
            
            tienda.save()
            
        return render(request, 'AppEntregaFinal/inicio.html')
    else:
        miFormulario = TiendaFormulario() #formulario vacio para construir el html
    return render(request, 'AppEntregaFinal/tiendas.html', {"miFormulario": miFormulario})

def clientes(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST) #donde llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid: #Si pasó la validacion de django
            informacion = miFormulario.cleaned_data
            
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], direccion=informacion['direccion'], telefono=informacion['telefono']) 
            
            cliente.save()
            
        return render(request, 'AppEntregaFinal/inicio.html')
    else:
        miFormulario = ClienteFormulario() #formulario vacio para construir el html
    return render(request, 'AppEntregaFinal/clientes.html', {"miFormulario": miFormulario})

def nosotros(request):
    return render(request, 'AppEntregaFinal/nosotros.html')

def categorias(request):
    if request.method == "POST":
        miFormulario = CategoriaFormulario(request.POST) #donde llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid: #Si pasó la validacion de django
            informacion = miFormulario.cleaned_data
            
            categoria = Categoria(nombre=informacion['nombre'], descripcion=informacion['descripcion']) 
                                         
            categoria.save()
            
        return render(request, 'AppEntregaFinal/inicio.html')
    else:
        miFormulario = CategoriaFormulario() #formulario vacio para construir el html
    return render(request, 'AppEntregaFinal/categorias.html', {"miFormulario": miFormulario})

def busquedaCategoria(request):
    return render(request, 'AppEntregaFinal/busquedaCategoria.html')
    #if request.GET['nombre']:
        
        #nombre = request.GET['nombre']
        #descripcion = Tienda.objects.filter(nombre__icontains=nombre)
            
        #return render(request, "AppEntregaFinal/inicio.html", {"nombre":nombre, "descripcion":descripcion})
    
    #else:
        #respuesta = "No enviaste datos"
    
    #return render(request, 'AppEntregaFinal/buscarCategoria.html', {'respuesta':respuesta})    
def buscar(request):
    #respuesta = f'Estoy buscando la categoria de nombre: {request.GET["nombre"]}'
    #return HttpResponse(respuesta)
    if request.GET['nombre']:
        
        nombre = request.GET['nombre']
        categoria = Categoria.objects.filter(nombre__icontains=nombre)
            
        return render(request, "AppEntregaFinal/resultadoBusqueda.html", {"categoria":categoria, "nombre":nombre})
    
    else:
        respuesta = "No enviaste datos"
    
    return render(request, 'AppEntregaFinal/busquedaCategoria.html', {'respuesta':respuesta}) 
