
from django.contrib import admin
from django.urls import path, include
from boxApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.inicio,name='inicio'),
    path('accounts/',include('django.contrib.auth.urls')),

    #EMPLEADOS
    path('empleadoAdd/',views.crear_empleado,name='crearEmpleados'),
    path('empleados/',views.mostrar_empleados,name='empleados'),
    path('empleadoCarga/<str:id>',views.cargar_empleado,name='cargarEmpleado'),
    path('modificarEmpleado/<str:id>',views.modificar_empleado,name='modificarEmpleado'),
    path('eliminarEmpleado/<str:id>',views.eliminar_empleado,name='eliminarEmpleado'),


    #ESPECIALIDADES
    path('especialidadAdd/',views.crear_especialidad,name='crearEspecialidades'),


    #PRODUCTOS
    path('productos/',views.mostrar_productos,name='productos'),
    path('productosAdd/',views.crear_producto,name='crearProductos'),
    path('productoCarga/<str:id>',views.cargar_producto,name='cargarProducto'),
    path('modificarProducto/<str:id>',views.modificar_producto,name='modificarProducto'),
    path('eliminarProducto/<str:id>',views.eliminar_producto,name='eliminarProducto'),


    #AREAS
    path('areaAdd/',views.crear_area,name='crearAreas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)