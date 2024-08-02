from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as especial

from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'evento', views.EventoViewSet)
router.register(r'mesa', views.MesaViewSet)
router.register(r'reserva', views.ReservaViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'producto', views.ProductoViewSet)
router.register(r'pedido', views.PedidoViewSet)
router.register(r'detalle_pedido', views.DetallePedidoViewSet)
router.register(r'compra_entrada', views.CompraEntradaViewSet)
#router.register(r'inventario', views.InventarioViewSet)
router.register(r'galeria', views.GaleriaViewSet)
router.register(r'fotos', views.FotosViewSet)
router.register(r'venta', views.VentaViewSet)
router.register(r'detalle_venta', views.DetalleVentaViewSet)


urlpatterns = [
    path('api/1.0/', include(router.urls)),
    path('api/1.0/token-auth/', views.CustomAuthToken.as_view()),
	path('api/1.0/api-auth/', include('rest_framework.urls')),
	path('api/1.0/token_qr/', views.token_qr.as_view()),





    path('', views.index, name="index"),
	path('inicio/', views.inicio, name="inicio"),


    #Autenticación de usuarios del sistema
    path('register/', views.crear_usuario_registro, name="usuario_registro"),
    path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),


    path('registro/', views.registro, name='registro'),

    #TÉRMINOS Y CONDICIONES
    path('tyc/', views.terminos_condiciones, name='tyc'),


    #PERFIL
    path('Perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('entradas/', views.entradas_usuario, name='entradas_usuario'),
    path('entradas_info/<int:id>/', views.entradas_usuario_info, name='entrada_info'),
    path('reservas/', views.reservas_usuario, name='reservas_usuario'),
    path('reservas_info/<int:id>/', views.reservas_usuario_info, name='reserva_info'),



    #CAMBIAR CONTRASEÑA
    path('cc_formulario/', views.cambio_clave_formulario, name="cc_formulario"),
    path('cambiar_clave/', views.cambiar_clave, name="cambiar_clave"),


    #RECUPERAR CONTRASEÑA
    path('recuperar_clave/', views.recuperar_clave, name="recuperar_clave"),
    path('verificar_recuperar/', views.verificar_recuperar, name="verificar_recuperar"),

    #USUARIOS
    path('Gestion_Usuarios/', views.guInicio, name='guInicio'),
    path('Usuarios_Bloqueados/', views.guUsuariosBloqueados, name='guUsuariosBloqueados'),

    path('Usuarios_Eliminados/<int:id>', views.guUsuariosEliminados, name='guUsuariosEliminados'),
    path('Usuarios_Actualizar/<int:id>', views.guUsuariosActualizar, name='guUsuariosActualizar'),
    path('guUsuariosCrear/', views.guUsuariosCrear, name='guUsuariosCrear'),


    #CRUD INVENTARIO
    #path('Gestion_Inventario/', views.invInicio, name='inventario'),
    #path('Agregar_Producto/', views.invForm, name='invForm'),
    #path('Crear_Inventario/', views.crearInventario, name='crearInventario'),
    #path('Eliminar_Inventario/<int:id>', views.eliminarInventario, name='eliminarInventario'),
    #path('Inventario_Actualizar/<int:id>', views.invFormActualizar, name='invFormActualizar'),
    #path('Actualizar_Inventario/', views.actualizarInventario, name='actualizarInventario'),


    #CRUD PRODUCTOS
    path('Gestion_Productos/', views.invProductos, name='Productos'),
    path('Crear_Producto/', views.crearProducto, name='crearProducto'),
    path('Eliminar_Producto/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('Actualizar_Producto/<int:id>', views.actualizarProducto, name='actualizarProducto'),


    #PEDIDOS
    path('Gestion_Pedidos/', views.peInicio, name='peInicio'),
    path('Historial_Pedidos/', views.ver_historial_pedidos, name='peHistorial'),
    path('Mesas/', views.peGestionMesas, name='peGestionMesas'),
    path('Agregar_Pedido/<int:id>', views.pedidoEmpleado, name='pedidoEmpleado'),
	path("crear_pedido/<int:id>", views.crear_pedido_admin, name="crear_pedido_admin"),

    #PEDIDOS USUARIO
    path('escanear_mesa/', views.escanear_mesa, name='escanear_mesa'),
    path('pedidoUsuario/<int:id>/', views.pedidoUsuario, name='pedidoUsuario'),
    path('crear_pedido_usuario/<int:id>', views.crear_pedido_usuario, name='crear_pedido_usuario'),



    #CRUD MESAS
    path('Gestion_Mesas/', views.mesaInicio, name='Mesas'),
    path('Agregar_Mesa/', views.crearMesa, name='crearMesa'),
    path('Actualizar_Mesa/<int:id>', views.mesaActualizar, name='mesaActualizar'),
    path('Eliminar_Mesa/<int:id>', views.eliminarMesa, name='eliminarMesa'),



#   CRUD EVENTOS
    path('Gestion_Eventos/', views.eveInicio, name='Eventos'),
    path('Agregar_Evento/', views.crearEvento, name='crearEvento'),
    path('Eliminar_Evento/<int:id>', views.eliminarEvento, name='eliminarEvento'),
    path('Actualizar_Evento/<int:id>', views.actualizarEvento, name='actualizarEvento'),
    path('Reservas/<int:id>', views.eveReserva, name='eveReserva'),
    path('Evento_Entradas/<int:id>', views.eveEntradas, name='eveEntradas'),
    path('Eliminar_Entrada/<int:id>', views.eliminarEntrada, name='eliminarEntrada'),

#   CRUD MENÚ (CATEGORÍAS)
    path('Gestion_Menu/', views.meInicio, name='Menu'),
    path('Crear_Categoria/', views.crearCategoria, name='crearCategoria'),
    path('Eliminar_Categoria/<int:id>', views.eliminarCategoria, name='eliminarCategoria'),
    path('Actualizar_Categoria/<int:id>', views.actualizarCategoria, name='actualizarCategoria'),
    path('Productos/', views.meProductos, name='meProductos'),


#   CRUD GALERÍA
    path('Gestion_Galeria/', views.gaInicio, name='gaInicio'),
    path('Agregar_Carpeta/', views.crearCarpeta, name='crearCarpeta'),
    path('Galeria_Fotos/', views.gaFotos, name='gaFotos'),
    path('Eliminar_Carpeta/<int:id>', views.eliminarCarpeta, name='eliminarCarpeta'),
    path('Actualizar_Carpeta/<int:id>', views.actualizarCarpeta, name='actualizarCarpeta'),



#   FRONT PRODUCTOS
    path('front_productos/', views.front_productos, name='front_productos'),
    path('front_productos_info/<int:id>/', views.front_productos_info, name='front_productos_info'),

#   FRONT EVENTOS
    path('front_eventos/', views.front_eventos, name='front_eventos'),
    path('front_eventos_info/<int:id>/', views.front_eventos_info, name='front_eventos_info'),


# CARRITO DE COMPRA USUARIO
	path("carrito_add/", views.carrito_add, name="carrito_add"),
	path("carrito_ver/", views.carrito_ver, name="carrito_ver"),
    path("carrito_eliminar/<int:id>/", views.carrito_eliminar, name="carrito_eliminar"),
	path("vaciar_carrito/", views.vaciar_carrito, name="vaciar_carrito"),
	path("actualizar_totales_carrito/<int:id_producto>/", views.actualizar_totales_carrito, name="actualizar_totales_carrito"),

#CARRITO DE COMPRA MESERO
	path("carrito_ver_admin/", views.carrito_ver_admin, name="carrito_ver_admin"),
	path("actualizar_totales_carrito_admin/<int:id_producto>/", views.actualizar_totales_carrito_admin, name="actualizar_totales_carrito_admin"),
    path("carrito_eliminar_admin/<int:id>/", views.carrito_eliminar_admin, name="carrito_eliminar_admin"),
	path("vaciar_carrito_admin/", views.vaciar_carrito_admin, name="vaciar_carrito_admin"),
    
    path('ver_pedidos_mesa/<int:mesa_id>/', views.ver_pedidos_mesa, name='ver_pedidos_mesa'),

    path('pagar_pedido/<int:id>/<str:rol>/', views.pagar_pedido, name='pagar_pedido'),
    path('entregar_pedido/<int:id>/', views.entregar_pedido, name='entregar_pedido'),
    path('cancelar_pedido/', views.cancelar_pedido, name='cancelar_pedido'),
    path('eliminar_producto/', views.eliminar_item, name='eliminar_producto'),
    path('liberar_mesa/<int:id>/', views.liberar_mesa, name='liberar_mesa'),




#VENTAS
	path("crear_venta/", views.crear_venta, name="crear_venta"),
	path("ver_ventas/", views.ver_pedidos_usuario, name="ver_ventas"),
	path("ver_detalles_pedido_usuario/", views.ver_detalles_usuario, name="ver_detalles_pedido_usuario"),

#COMPRAR ENTRADAS
    path("comprar_entradas/<int:id>/", views.comprar_entradas, name="comprar_entradas"),

#RESERVAR MESAS
    path("reservar_mesa/<int:id>/", views.reservar_mesa, name="reservar_mesa"),

# mas información
    path('mas_info/', views.mas_info, name='mas_info'),
]   