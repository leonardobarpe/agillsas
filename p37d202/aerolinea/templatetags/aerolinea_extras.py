from django import template
from aerolinea.models import Componente
from aerolinea.models import Aeronave
from aerolinea.models import Orden

register = template.Library()

@register.simple_tag
def get_componente_list():
	componentes = Componente.objects.all()
	return componentes

@register.simple_tag
def get_aeronave_list():
	aeronaves = Aeronave.objects.all()
	return aeronaves

@register.simple_tag
def get_orden_list():
	ordenes = Orden.objects.all()
	return ordenes