from ckeditor.fields import RichTextField
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models import *


# Create your models here.

class Componente(models.Model):
	numSerie			= models.CharField(max_length=200, verbose_name="Numero de Serie")					
	nombre				= models.CharField(max_length=200, verbose_name="Nombre")							
	marca				= models.CharField(max_length=200, verbose_name="Parte/Numero")							
	
	fechaingreso		= models.DateField(verbose_name="Fecha de Instalacion")									
	mesesVencimiento	= models.IntegerField(verbose_name="Meses de vencimiento",default=1, blank=True)
	fechaVencimiento	= models.DateField(verbose_name="Fecha de Vencimiento")								
	
	fabricante			= models.CharField(max_length=200, verbose_name="Fabricante")						
	proveedor			= models.CharField(max_length=200, verbose_name="Proveedor")						
	
	tipo1='t1'
	tipo2='t2'
	opcTipo = (
		(tipo1, 'Tipo 1'),
		(tipo2, 'Tipo 2'),
	)
	tipo			= models.CharField(max_length=20, verbose_name="Tipo componente", choices=opcTipo, default=tipo1, null=True)	
	
	HORAS='h'
	TIEMPO='t'
	AMBOS='a'
	opcVutil = (
		(HORAS, 'Horas'),
		(TIEMPO, 'Tiempo'),
		(AMBOS, 'Ambos'),
	)
	vUtilOpc			= models.CharField(max_length=20, verbose_name="TBO", choices=opcVutil, default=HORAS, null=True, blank=True)
	vUtil				= models.DateField(verbose_name="TBO Calendario",null=True, blank=True)
	hvUtil 				= models.IntegerField(verbose_name="Horas TBO",default=1, blank=True)
	mvUtil 				= models.IntegerField(verbose_name="Minutos TBO",default=1, blank=True)

	HORAS_i='h'
	TIEMPO_i='t'
	AMBOS_i='a'
	opcVutil_i = (
		(HORAS_i, 'Horas'),
		(TIEMPO_i, 'Tiempo'),
		(AMBOS_i, 'Ambos'),
	)
	vUtilOpc_i			= models.CharField(max_length=20, verbose_name="TBO inspeccion inicial", choices=opcVutil_i, default=HORAS_i, null=True, blank=True)
	vUtil_i				= models.DateField(verbose_name="TBO Calendario inspec inicial",null=True, blank=True)
	hvUtil_i			= models.IntegerField(verbose_name="Horas inspec inicial TBO",default=1, blank=True)	
	mvUtil_i 			= models.IntegerField(verbose_name="Minutos inspec inicial TBO",default=1, blank=True)

	HORAS_p='h'
	TIEMPO_p='t'
	AMBOS_p='a'
	opcVutil_p = (
		(HORAS_p, 'Horas'),
		(TIEMPO_p, 'Tiempo'),
		(AMBOS_p, 'Ambos'),
	)
	vUtilOpc_p			= models.CharField(max_length=20, verbose_name="TBO inspeccion posterior", choices=opcVutil_p, default=HORAS_p, null=True, blank=True)
	vUtil_p				= models.DateField(verbose_name="TBO Calendario inspec posterior",null=True, blank=True)
	hvUtil_p			= models.IntegerField(verbose_name="Horas inspec posterior TBO",default=1, blank=True)	
	mvUtil_p 			= models.IntegerField(verbose_name="Minutos inspec posterior TBO",default=1, blank=True)
	
	ordenTrabajo		= models.CharField(max_length=20, verbose_name="Orden Trabajo", default="OT7")
	hUtilizado			= models.IntegerField(verbose_name="Horas total", default=1, blank=True)			
	mUtilizado			= models.IntegerField(verbose_name="Minutos total",default=1, blank=True)
	hDurg				= models.IntegerField(verbose_name="Horas Durg", default=1, blank=True)				
	mDurg				= models.IntegerField(verbose_name="Minutos Durg",default=1, blank=True)

	descripcion			= models.CharField(max_length=200, verbose_name="Descripcion",null=True, blank=True)

	hRemanente			= models.IntegerField(verbose_name="Horas Remanente", default=1)		
	mRemanente			= models.IntegerField(verbose_name="Minutos Remanente",default=1)
	porcenUso			= models.IntegerField(verbose_name="Porcentaje de uso",default=1)
	
	alerta				= models.CharField(max_length=20, verbose_name="Alerta", default="No")
	alerta_i			= models.CharField(max_length=20, verbose_name="Alerta inicial", default="No")
	alerta_p			= models.CharField(max_length=20, verbose_name="Alerta posterior", default="No")
	
	alertaFecha			= models.CharField(max_length=20, verbose_name="Alerta fecha", default="No")
	alertaFecha_i		= models.CharField(max_length=20, verbose_name="Alerta fecha inicial", default="No")
	alertaFecha_p		= models.CharField(max_length=20, verbose_name="Alerta fecha posterior", default="No")
	
	
	hRemanente_i		= models.IntegerField(verbose_name="Horas Remanente inicial", default=1)
	mRemanente_i		= models.IntegerField(verbose_name="Minutos Remanente inicial", default=1)

	hRemanente_p		= models.IntegerField(verbose_name="Horas Remanente posterior", default=1)
	mRemanente_p		= models.IntegerField(verbose_name="Minutos Remanente posterior", default=1)
	
	porcenUso_i			= models.IntegerField(verbose_name="Porcentaje de uso inicial",default=1)
	porcenUso_p			= models.IntegerField(verbose_name="Porcentaje de uso posterior",default=1)

	estado				= models.CharField(max_length=200, verbose_name="Estado", null=True)
	fechaFabricacion	= models.DateField(verbose_name="Fecha de Fabricacion",null=True)							
	# -- Auditoria -- #
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)
	actualizado			= models.DateTimeField(auto_now = True, null=True, blank=True)

	def asignado(self):
		return self.aeronave.all().count() > 0

	def horasRemanentes(self):
		return self.hvUtil - self.hDurg

	def horasRemanentes_i(self):
		return self.hvUtil_i - self.hDurg

	def horasRemanentes_p(self):
		return self.hvUtil_p - self.hDurg			

	def porcentaUso(self):
		return (self.hDurg * 100)/self.hvUtil

	def porcentaUso_i(self):
		return (self.hDurg * 100)/self.hvUtil_i

	def porcentaUso_p(self):
		return (self.hDurg * 100)/self.hvUtil_p


	# -- ADMIN --#
	class Meta:
		verbose_name = "Componente"					# nombre en el admin
		verbose_name_plural = "Componentes"			# nombre en el admin en plural
		ordering = ['-creado']						# orden en el admin (por defecto es antiguo al nuevo) con el - lo hace al inverso

	def __str__(self):
		return '%s %s %s %s %s' %(self.numSerie, "-", self.id, "-", self.nombre,) 		# devuelve numero de serie - el nombre del componente

Componente.objects.all().update(
	# hvUtil=10,
	# mvUtil=10,
	# hvUtil_i=10,
	# mvUtil_i=10,
	# hvUtil_p=10,
	# mvUtil_p=10,
	# hUtilizado=10,
	# mUtilizado=10,
	# hDurg=10,
	# mDurg=10,
	hRemanente = F('hvUtil') - F('hDurg'),
	mRemanente = F('mvUtil') - F('mDurg'),
	hRemanente_i = F('hvUtil_i') - F('hDurg'),
	mRemanente_i = F('mvUtil_i') - F('mDurg'),
	hRemanente_p = F('hvUtil_p') - F('hDurg'),
	mRemanente_p = F('mvUtil_p') - F('mDurg'),
	porcenUso = (F('hDurg')*100)/F('hvUtil'),
	porcenUso_i = (F('hDurg')*100)/F('hvUtil_i'),
	porcenUso_p = (F('hDurg')*100)/F('hvUtil_p'),
)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

class Aeronave(models.Model):
	placa				= models.CharField(max_length=200, verbose_name="Matricula")							# placa de la aeronave
	marca				= models.CharField(max_length=200, verbose_name="Marca")								# marca de la aeronave
	modelo				= models.CharField(max_length=200, verbose_name="Modelo")								# modelo de la aeronave
	tipo				= models.CharField(max_length=200, verbose_name="Tipo")									# tipo de la aeronave
	descripcion			= models.TextField(verbose_name="Descripcion", null=True, blank=True)					# descripcion de la aeronave
	imagen				= models.ImageField(upload_to="Aeronave", verbose_name="Imagen", null=True, blank=True)	# imagen de la aeronave
	hVuelo				= models.IntegerField(verbose_name="Horas de Vuelo", null=True, blank=True)				# horas de vuelo de la aeronave 
	mVuelo				= models.IntegerField(verbose_name="Minutos de Vuelo", null=True, blank=True)			# minutos de vuelo de la aeronave
	alerta				= models.CharField(max_length=20, verbose_name="Alerta", default="No")
	ordenCom			= models.CharField(max_length=300, verbose_name="Orden componentes", null=True, blank=True)	# Orden en el que se selecionan los componentes
	# -- Auditoria -- 	#
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)						# Registra fecha al crearlo
	actualizado			= models.DateTimeField(auto_now = True, null=True, blank=True)							# Registra fecha al actualizarlo
	# -- Llaves -- #
	componente			= models.ManyToManyField(Componente, blank=True, verbose_name="Componentes")
	# -- ADMIN -- #
	class Meta:
		verbose_name = "Aeronave"						# Nombre en el admin
		verbose_name_plural = "Aeronaves"				# Nombre en el admin en plural
		ordering = ['-creado']							# orden en el admin (por defecto es antiguo al nuevo) con el - lo hace al inverso

	def __str__(self):
		return '%s %s %s' %(self.placa, "-", self.modelo) 		# valores que devuel al llamarlo en el views

	def getComponenteOrdenado(self):
		return self.componente.through.objects.filter(aeronave=self).order_by('id')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class Vuelo(models.Model):
	fecha				= models.DateField(verbose_name="Fecha de vuelo")									# Fecha del vuelo
	origen				= models.CharField(max_length=200, verbose_name="Origen")							# Sitio de origen del vuelo
	destino				= models.CharField(max_length=200, verbose_name="Destino")							# Sitio de destino del vuelo
	horas				= models.IntegerField(verbose_name="Horas de vuelo", null=True)		# Horas de vuelo
	minutos				= models.IntegerField(verbose_name="Minutos de vuelo", null=True)		# minutos de vuelo
	observaciones		= models.TextField(verbose_name="Observaciones", null=True)							# Observaciones del vuelo
	# -- Auditoria -- #
	creado				= models.DateTimeField(auto_now_add = True,null=True, blank=True)					# Registra fecha al crearlo
	actualizado			= models.DateTimeField(auto_now = True)												# Registra fecha al crearlo
	# -- Llaves --#
	aeronave 			= models.ForeignKey(Aeronave, on_delete=models.CASCADE)
	# -- ADMIN -- #
	class Meta:
		verbose_name = "Vuelo"						# nombre en el admin
		verbose_name_plural = "Vuelos"				# nombre en el admin en plural
		ordering = ['-creado']						# orden en el admin (por defecto es antiguo al nuevo) con el - lo hace al inverso

	def __str__(self):
		return '%s %s %s %s' %(self.fecha, "-", self.origen, self.destino) 		# valores que devuel al llamarlo en el views



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Orden(models.Model):
	ciudad			= models.CharField(max_length=200, verbose_name="Ciudad")
	fecha 			= models.DateField(verbose_name="Fecha de Orden")
	descripcion		= models.TextField(verbose_name="Descripcion")
	tecnico			= models.CharField(max_length=200, verbose_name="Tecnico")
	dirCC			= models.CharField(max_length=200, verbose_name="Director control calidad")
	# -- Auditoria -- #
	creado				= models.DateTimeField(auto_now_add = True,null=True, blank=True)
	actualizado			= models.DateTimeField(auto_now = True)	
	# -- Llaves --#
	aeronave 		= models.ForeignKey(Aeronave, verbose_name="Aeronave", on_delete=models.CASCADE)
	componente		= models.ManyToManyField(Componente, blank=True, verbose_name="Componente(s)")
	# -- ADMIN -- #
	class Meta:
		verbose_name = "Orden"						
		verbose_name_plural = "Ordenes"	
		ordering = ['-creado']						

	def __str__(self):
		return '%s %s %s %s' %(self.id, "-", self.aeronave, self.fecha)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class Mantenimiento(models.Model):
	fecha				= models.DateField()							# Fecha del mantenimiento
	descripcion			= models.TextField()							# Descripcion del mantenimiento
	# --------------------------------------------------- Auditoria --------------------------------------------------------- #
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)		# Registra fecha al crearlo
	actualizado			= models.DateTimeField(auto_now = True)			# Registra fecha al crearlo

class Cumplimiento(models.Model):
	fecha				= models.DateField()							# Fecha del cumplimiento
	nombre				= models.CharField(max_length=200)				# nombre del cumplimiento
	codigo				= models.CharField(max_length=200)				# nombre del cumplimiento
	# --------------------------------------------------- Auditoria --------------------------------------------------------- #
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)		# Registra fecha al crearlo
	actualizado			= models.DateTimeField(auto_now = True)			# Registra fecha al crearlo

class ItemCumplimiento(models.Model):
	codigo				= models.CharField(max_length=200)				# nombre del item cumplimiento
	titulo				= models.TextField()							# titulo del item cumplimiento
	metoCumplimiento	= models.TextField()							# metodo de cumplimiento del item cumplimiento
	metoInspeccion		= models.CharField(max_length=200)				# metodo de inspeccion del item cumplimiento
	proximo				= models.CharField(max_length=200)				# proximo tiempo o fecha del item cumplimiento
	tecnico				= models.CharField(max_length=200)				# tecnico del item cumplimiento
	inspector			= models.CharField(max_length=200)				# inspctor del item cumplimiento
	# --------------------------------------------------- Auditoria --------------------------------------------------------- #
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)		# Registra fecha al crearlo
	actualizado			= models.DateTimeField(auto_now = True)			# Registra fecha al crearlo