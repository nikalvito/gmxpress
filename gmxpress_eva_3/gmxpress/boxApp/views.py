from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from boxApp.forms import EmpleadoForm,EspecialidadForm,AreaForm,ProductoForm
from boxApp.models import Empleado,Area,Especialidad,Producto

# Create your views here.
def inicio(request):
    return render(request,'templatesBoxApp/inicio.html')

#EMPLEADOS
@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/empleados/')
    else:
        form = EmpleadoForm()

    return render(request,'templatesBoxApp/empleadoAdd.html',{'form':form})


@login_required
def mostrar_empleados(request):
    empleados = Empleado.objects.all()
    areas = Area.objects.all()
    especialidades = Especialidad.objects.all()

    data = {
        'empleados' : empleados,
        'areas' : areas,
        'especialidades' : especialidades
    }

    return render(request,'templatesBoxApp/empleados.html',data)

@login_required
def cargar_empleado(request,id):
    empleado = get_object_or_404(Empleado,id=id)
    form = EmpleadoForm(instance=empleado)

    return render(request,'templatesBoxApp/empleadoEdit.html',{'form':form, 'empleado':empleado})

@login_required
def modificar_empleado(request,id):
    empleado = get_object_or_404(Empleado,id=id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST,request.FILES,instance=empleado)
        if form.is_valid():
            if 'foto' in request.FILES:
                empleado.foto = request.FILES['foto']
            form.save()
            return redirect('/empleados/')
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request,'templatesBoxApp/empleadoEdit.html',{'form':form, 'empleado':empleado})

@login_required
def eliminar_empleado(request,id):
    empleado = get_object_or_404(Empleado,id=id)

    if request.method == 'POST':
        empleado.delete()
        return redirect('/empleados/')

    return render(request,'templatesBoxApp/eliminarEmpleado.html',{'empleado':empleado})


#ESPECIALIDADES
@login_required
def crear_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/especialidades/')
    else:
        form = EspecialidadForm()

    return render(request,'templatesBoxApp/especialidadAdd.html',{'form':form})

#AREAS
@login_required
def crear_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/areas/')
    else:
        form = AreaForm()

    return render(request,'templatesBoxApp/areaAdd.html',{'form':form})

#PRODUCTOS
@login_required
def mostrar_productos(request):
    productos = Producto.objects.all()

    return render(request,'templatesBoxApp/productos.html',{'productos':productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm()

    return render(request,'templatesBoxApp/productosAdd.html',{'form':form})

@login_required
def cargar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    form = ProductoForm(instance=producto)

    return render(request,'templatesBoxApp/productoEdit.html',{'form':form, 'producto':producto})

@login_required
def modificar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm(instance=producto)

    return render(request,'templatesBoxApp/productoEdit.html',{'form':form, 'producto':producto})

@login_required
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('/productos/')

    return render(request,'templatesBoxApp/eliminarProducto.html',{'producto':producto})
