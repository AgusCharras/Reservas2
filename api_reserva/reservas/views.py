from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Reserva, Cliente, Encargado, Complejo, Cabania, Servicio
<<<<<<< HEAD
from .forms import formCabania, formEncargado, formCliente, formComplejo, formServicio, formReserva
=======
from .forms import formCabania
>>>>>>> 49f73bc3c3687db73288632ede484512c8d311bc

# Create your views here.

def main(request):
    reservas = Reserva.objects.all()
    clientes = Cliente.objects.all()
    encargados = Encargado.objects.all()
    complejos = Complejo.objects.all()
    cabanias = Cabania.objects.all()
    servicios = Servicio.objects.all()

    context = {'reservas': reservas,
               'clientes': clientes,
               'encargados': encargados,
               'complejos': complejos,
               'cabanias': cabanias,
               'servicios':servicios}
    
    return render(request, 'main.html', context)

def tabla_reservas(request):
    reservas = Reserva.objects.all()

    context = {'reservas': reservas}
    return render(request, 'reservas.html', context)

def tabla_clientes(request):
    clientes = Cliente.objects.all()

    context = {'clientes': clientes}
    return render(request, 'clientes.html', context)

def tabla_encargados(request):
    encargados = Encargado.objects.all()

    context = {'encargados': encargados}
    return render(request, 'encargados.html', context)

def tabla_complejos(request):
    complejos = Complejo.objects.all()

    context = {'complejos': complejos}
    return render(request, 'complejos.html', context)

def tabla_cabanias(request):
    cabanias = Cabania.objects.all()

    context = {'cabanias': cabanias}
    return render(request, 'cabanias.html', context)

def tabla_servicios(request):
    servicios = Servicio.objects.all()

    context = {'servicios': servicios}
    return render(request, 'servicios.html', context)

def detalle_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id) #solo toma el id del cliente         #toma todos los atributos del cliente

    context = {
        'cliente': cliente
    }
    return render(request, 'detalle_cliente.html', context)

def detalle_encargado(request, encargado_id):
    encargado = Encargado.objects.get(id=encargado_id)

    context={
        'encargado': encargado
    }
    return render(request,'detalle_encargado.html', context)

def detalle_complejo(request, complejo_id):
    complejo = Complejo.objects.get(id=complejo_id)

    context = {
        'complejo': complejo
    }
    return render(request, 'detalle_complejo.html', context)

def detalle_cabania(request, cabania_id):
    cabania = Cabania.objects.get(id=cabania_id)

    context = {
        'cabania': cabania
    }
    return render(request, 'detalle_cabania.html', context)

def detalle_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)

    context = {
        'reserva': reserva
    }
    return render(request, 'detalle_reserva.html', context)

def detalle_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)

    context = {
        'servicio': servicio
    } 
    return render(request, 'detalle_servicio.html', context)

#abm encargado

def modif_encargado(request, pk):
    encargado = Encargado.objects.get(id=pk)
    if request.method=='POST':
        form = formEncargado(request.POST, instance=encargado)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_encargados'))
        
    else:
        form = formEncargado(instance=encargado)

    return render(request, 'form_encargado.html', {'form': form,'encargado': encargado})

def nuevo_encargado(request):
    if request.method=='POST':
        form = formEncargado(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_encargados'))
        
    else:
        form = formEncargado()
    
    return render(request, 'form_encargado.html', {'form': form})

def borrar_encargado(request, pk):
    encargado = Encargado.objects.get(id=pk)
    if request.method=='POST':
        encargado.delete()
        return HttpResponseRedirect(reverse('tabla_encargados'))
    return render(request, 'conf_borrar_encargado.html', {'encargado': encargado})

<<<<<<< HEAD
#abm cabañas
=======
#abm clientes

def modif_cliente(request, pk):
    cliente = Cliente.objects.get(dni=pk)

    if request.method == 'POST':
        dni = request.POST.get('dni')
        apellido_nombre = request.POST.get('apellido_nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        pais = request.POST.get('pais')
        provincia = request.POST.get('provincia')
        localidad = request.POST.get('localidad')

        cliente.dni = dni
        cliente.apellido_nombre = apellido_nombre
        cliente.telefono = telefono
        cliente.email = email
        cliente.pais = pais
        cliente.provincia = provincia
        cliente.localidad = localidad
        cliente.save()

        return HttpResponseRedirect(reverse('tabla_clientes'))
    return render(request, "form_cliente.html", {'cliente': cliente})

def nuevo_cliente(request):
    if request.method=='POST':
        dni = request.POST.get('dni')
        apellido_nombre = request.POST.get('apellido_nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        pais = request.POST.get('pais')
        provincia = request.POST.get('provincia')
        localidad = request.POST.get('localidad')

        Cliente.objects.create(dni=dni, apellido_nombre=apellido_nombre, telefono=telefono, email=email, pais=pais, provincia=provincia, localidad=localidad)

        return HttpResponseRedirect(reverse('tabla_clientes'))
    return render(request, "form_cliente.html")

>>>>>>> 49f73bc3c3687db73288632ede484512c8d311bc
def modif_cabania(request, pk):
    cabania = Cabania.objects.get(id=pk)
    if request.method=='POST':
        form = formCabania(request.POST, instance=cabania)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_cabanias'))
        
    else:
        form = formCabania(instance=cabania)

    return render(request, 'form_cabania.html', {'form': form,'cabania': cabania})

def nuevo_cabania(request):
    if request.method=='POST':
        form = formCabania(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_cabanias'))
        
    else:
        form = formCabania()
    
    return render(request, 'form_cabania.html', {'form': form})

def borrar_cabania(request, pk):
    cabania = Cabania.objects.get(id=pk)
    if request.method=='POST':
        cabania.delete()
        return HttpResponseRedirect(reverse('tabla_cabanias'))
    return render(request, 'conf_borrar_cabania.html', {'cabania': cabania})

<<<<<<< HEAD
#abm cliente
def modif_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method=='POST':
        form = formCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_clientes'))
        
    else:
        form = formCliente(instance=cliente)

    return render(request, 'form_cliente.html', {'form': form,'cliente': cliente})

def nuevo_cliente(request):
    if request.method=='POST':
        form = formCliente(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_clientes'))
        
    else:
        form = formCliente()
    
    return render(request, 'form_cliente.html', {'form': form})

def borrar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method=='POST':
        cliente.delete()
        return HttpResponseRedirect(reverse('tabla_cliente'))
    return render(request, 'conf_borrar_cliente.html', {'cliente': cliente})

#abm complejo
def modif_complejo(request, pk):
    complejo = Complejo.objects.get(id=pk)
    if request.method=='POST':
        form = formComplejo(request.POST, instance=complejo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_complejos'))
        
    else:
        form = formComplejo(instance=complejo)

    return render(request, 'form_complejo.html', {'form': form,'complejo': complejo})

def nuevo_complejo(request):
    if request.method=='POST':
        form = formComplejo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_complejos'))
        
    else:
        form = formComplejo()
    
    return render(request, 'form_complejo.html', {'form': form})

def borrar_complejo(request, pk):
    complejo = Complejo.objects.get(id=pk)
    if request.method=='POST':
        complejo.delete()
        return HttpResponseRedirect(reverse('tabla_complejos'))
    return render(request, 'conf_borrar_complejo.html', {'complejo': complejo})

#abm servicios
def modif_servicio(request, pk):
    servicio = Servicio.objects.get(id=pk)
    if request.method=='POST':
        form = formServicio(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_servicios'))
        
    else:
        form = formServicio(instance=servicio)

    return render(request, 'form_servicio.html', {'form': form,'servicio': servicio})

def nuevo_servicio(request):
    if request.method=='POST':
        form = formServicio(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_servicios'))
        
    else:
        form = formServicio()
    
    return render(request, 'form_servicio.html', {'form': form})

def borrar_servicio(request, pk):
    servicio = Servicio.objects.get(id=pk)
    if request.method=='POST':
        servicio.delete()
        return HttpResponseRedirect(reverse('tabla_servicios'))
    return render(request, 'conf_borrar_servicio.html', {'servicio': servicio})

#abm reservas
def modif_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    if request.method=='POST':
        form = formReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_reservas'))
        
    else:
        form = formReserva(instance=reserva)

    return render(request, 'form_reserva.html', {'form': form,'reserva': reserva})

def nuevo_reserva(request):
    if request.method=='POST':
        form = formReserva(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_reservas'))
        
    else:
        form = formReserva()
    
    return render(request, 'form_reserva.html', {'form': form})

def borrar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    if request.method=='POST':
        reserva.delete()
        return HttpResponseRedirect(reverse('tabla_reservas'))
    return render(request, 'conf_borrar_reserva.html', {'reserva': reserva})
=======
>>>>>>> 49f73bc3c3687db73288632ede484512c8d311bc
