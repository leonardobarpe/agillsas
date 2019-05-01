"""p37d202 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from core import views as core_views
from aerolinea import views as aerolinea_views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),

    # - Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),


    # Core 
    # path('', include('core.urls')),
    path('', core_views.inicio, name ='inicio'),

    # - Componentes -#
    path('componente/componenteListView', aerolinea_views.componenteListView.as_view(), name = 'componente_list'),
    path('componente/<int:pk>/',aerolinea_views.componenteDetailView.as_view(), name = 'componente_detail'),
    path('componente/componenteCreateView',aerolinea_views.componenteCreateView.as_view(), name = 'componente_create'),
    path('componente/componenteUpdateView/<int:pk>/',aerolinea_views.componenteUpdateView.as_view(), name = 'componente_update'),
    path('componente/componenteDeleteView/<int:pk>/',aerolinea_views.componenteDeleteView.as_view(), name = 'componente_delete'),
    path('componente/componenteDownExcel',aerolinea_views.componenteDownExcel, name = 'componente_downExcel'),
    path('componente/componentePDFDetailView/<int:pk>/',aerolinea_views.componentePDFDetailView.as_view(), name = 'componente_pdf_detail'),
    
    

    # *******************************
    path('componente/componente_lista', aerolinea_views.componente_lista, name = 'componente_lista'),
    path('componente/<int:componente_id>/', aerolinea_views.componente_info, name = 'componente_info'),
    path('componente/componente_nuevo/', aerolinea_views.componente_nuevo, name = 'componente_nuevo'),
    
    # - Aeronave - #
    path('aeronave/aeronaveListView', aerolinea_views.aeronaveListView.as_view(), name = 'aeronave_list'),
    path('aeronave/<int:pk>/',aerolinea_views.aeronaveDetailView.as_view(), name = 'aeronave_detail'),
    path('aeronave/aeronaveCreateView',aerolinea_views.aeronaveCreateView.as_view(), name = 'aeronave_create'),
    path('aeronave/aeronaveUpdateView/<int:pk>/',aerolinea_views.aeronaveUpdateView.as_view(), name = 'aeronave_update'),
    path('aeronave/aeronaveDeleteView/<int:pk>/',aerolinea_views.aeronaveDeleteView.as_view(), name = 'aeronave_delete'),
    path('aeronave/aeronavePDFListView/',aerolinea_views.aeronavePDFListView.as_view(), name = 'aeronave_pdf_list'),
    path('aeronave/aeronavePDFDetailView/<int:pk>/',aerolinea_views.aeronavePDFDetailView.as_view(), name = 'aeronave_pdf_detail'),
    
    path('aeronave/aeronaveDownExcel',aerolinea_views.aeronaveDownExcel, name = 'aeronave_downExcel'),
    path('aeronave/aeronaveReporteExcel',aerolinea_views.aeronaveReporteExcel.as_view(), name = 'aeronave_reporteExcel'),

    

    # ****************************************
    path('aeronave/aeronave_lista', aerolinea_views.aeronave_lista, name = 'aeronave_lista'),
    path('aeronave/<int:aeronave_id>/', aerolinea_views.aeronave_info, name = 'aeronave_info'),

    # - Vuelo - #
    path('vuelo/vueloListView',aerolinea_views.vueloListView.as_view(), name = 'vuelo_list'),
    path('vuelo/<int:pk>/',aerolinea_views.vueloDetailView.as_view(), name = 'vuelo_detail'),
    path('vuelo/vueloCreateView',aerolinea_views.vueloCreateView.as_view(), name = 'vuelo_create'),
    path('vuelo/vueloUpdateView/<int:pk>/',aerolinea_views.vueloUpdateView.as_view(), name = 'vuelo_update'),
    path('vuelo/vueloDeleteView/<int:pk>/',aerolinea_views.vueloDeleteView.as_view(), name = 'vuelo_delete'),

    # - Orden - #
    path('orden/ordenListView',aerolinea_views.ordenListView.as_view(), name = 'orden_list'),
    path('orden/<int:pk>/',aerolinea_views.ordenDetailView.as_view(), name = 'orden_detail'),
    path('orden/ordenCreateView',aerolinea_views.ordenCreateView.as_view(), name = 'orden_create'),
    path('orden/ordenCrear',aerolinea_views.ordenCrear.as_view(), name = 'orden_crear'),

    path('orden/ordenUpdateView/<int:pk>/',aerolinea_views.ordenUpdateView.as_view(), name = 'orden_update'),
    path('orden/ordenDeleteView/<int:pk>/',aerolinea_views.ordenDeleteView.as_view(), name = 'orden_delete'),
    path('orden/ordenPDFListView/',aerolinea_views.ordenPDFListView.as_view(), name = 'orden_pdf_list'),
    path('orden/ordenPDFDetailView/<int:pk>/',aerolinea_views.ordenPDFDetailView.as_view(), name = 'orden_pdf_detail'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Nombre del encabezado del admin
admin.site.site_header = 'Administrador - Agillsas'