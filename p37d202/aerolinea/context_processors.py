from aerolinea.models import *

def componeteDisponible(request):
	return {'componente_alerta': Componente.objects.filter(alerta = "Si")}