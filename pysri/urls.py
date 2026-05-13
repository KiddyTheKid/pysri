from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authtoken import views
from pysri.views import UserViewSet
from clientes.views import ClientesViewSet
from productos.views import ProductosViewSet
from empresas.views import EmpresaViewSet
from facturas.views import FacturasViewSet


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"clientes", ClientesViewSet)
router.register(r"productos", ProductosViewSet)
router.register(r"empresas", EmpresaViewSet)
router.register(r"facturas", FacturasViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
    path("auth-token/", views.obtain_auth_token),
]
