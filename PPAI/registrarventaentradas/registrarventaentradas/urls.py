"""registrarventaentradas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rve.views import opciones, opcionVentaEntrada, montoSinGuia, montoConGuia, tomarSeleccionTarifa, cantidadEntradasAEmitir, tomarVentaConfirmada, pantallaVisitantesSede, pantallaPrincipal,pantallaVisitantesSedeDos,pantallaVisitantesSedeTres
urlpatterns = [
    path('', opciones),
    path('admin/', admin.site.urls),
    path('opciones/', opciones),
    path('venta/', opcionVentaEntrada),
    path('montosinguia/', montoSinGuia),
    path('montoconguia/', montoConGuia),
    path('duracion/', tomarSeleccionTarifa),
    path('cantEntradasSelec/',cantidadEntradasAEmitir),
    path('error/', cantidadEntradasAEmitir ),
    path('confirmada/', tomarVentaConfirmada),
    path('pantallaVisitantesSede/', pantallaVisitantesSede),
    path('pantallaVisitantesSedeDos/', pantallaVisitantesSedeDos ),
    path('pantallaVisitantesSedeTres/', pantallaVisitantesSedeTres ),
    path('pantallaPrincipal/', pantallaPrincipal )

]

