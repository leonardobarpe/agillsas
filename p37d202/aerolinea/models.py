from ckeditor.fields import RichTextField
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models import *


# Create your models here.

class Componente(models.Model):
	numSerie			= models.CharField(max_length=200, verbose_name="Numero de Serie")					
	nombre				= models.CharField(max_length=200, verbose_name="Nombre")							
	marca				= models.CharField(max_length=200, verbose_name="Marca /P-N o Modelo")							
	fabricante			= models.CharField(max_length=200, verbose_name="Fabricante")						
	fechaFabricacion	= models.DateField(verbose_name="Fecha de Fabricacion")								
	fechaVencimiento	= models.DateField(verbose_name="Fecha de Vencimiento")								
	proveedor			= models.CharField(max_length=200, verbose_name="Proveedor")						
	fechaingreso		= models.DateField(verbose_name="Fecha de Ingreso")									
	descripcion			= models.CharField(max_length=200, verbose_name="Descripcion",null=True, blank=True)
	# -- Vida util --#
	HORAS='h'
	TIEMPO='t'
	AMBOS='a'
	opcVutil = (
		(HORAS, 'Horas'),
		(TIEMPO, 'Tiempo'),
		(AMBOS, 'Ambos'),
	)
	vUtilOpc			= models.CharField(max_length=20, verbose_name="Vida Util", choices=opcVutil, default=HORAS)
	vUtil				= models.DateField(verbose_name="Vida Util Calendario",null=True, blank=True)
	hvUtil 				= models.IntegerField(verbose_name="Horas de vida util",null=True, blank=True, default=1)		
	mvUtil 				= models.IntegerField(verbose_name="Minutos de vida util",null=True, blank=True)	
	# -- -- #
	hUtilizado			= models.IntegerField(verbose_name="Horas utilizado",null=True, blank=True)			
	mUtilizado			= models.IntegerField(verbose_name="Minutos utilizado",null=True, blank=True)		
	hDurg				= models.IntegerField(verbose_name="Horas Durg",null=True, blank=True)				
	mDurg				= models.IntegerField(verbose_name="Minutos Durg",null=True, blank=True)			
	hRemanente			= models.IntegerField(verbose_name="Horas Remanente",null=True, blank=True)			
	mRemanente			= models.IntegerField(verbose_name="Minutos Remanente",null=True, blank=True)
	porcenUso			= models.IntegerField(verbose_name="Porcentaje de uso",default=1)	
	estado				= models.CharField(max_length=200, verbose_name="Estado")
	alerta				= models.CharField(max_length=20, verbose_name="Alerta", default="No")
	# -- Auditoria -- #
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)
	actualizado			= models.DateTimeField(auto_now = True, null=True, blank=True)


	def horasRemanentes(self):
		return self.hvUtil - self.hDurg

	def porcentaUso(self):
		return (self.hDurg * 100)/self.hvUtil


	# -- ADMIN --#
	class Meta:
		verbose_name = "Componente"					# nombre en el admin
		verbose_name_plural = "Componentes"			# nombre en el admin en plural
		ordering = ['-creado']						# orden en el admin (por defecto es antiguo al nuevo) con el - lo hace al inverso

	def __str__(self):
		return '%s %s %s' %(self.numSerie, "-", self.nombre) 		# devuelve numero de serie - el nombre del componente

Componente.objects.all().update(
	porcenUso = (F('hDurg')*100)/F('hvUtil'),
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
	# -- Auditoria -- 	#
	creado				= models.DateTimeField(auto_now_add = True, null=True, blank=True)						# Registra fecha al crearlo
	actualizado			= models.DateTimeField(auto_now = True, null=True, blank=True)							# Registra fecha al actualizarlo
	# -- Llaves -- #
	componente			= models.ManyToManyField(Componente, blank=True, verbose_name="Componentes")
	ordenCom			= models.CharField(max_length=300, verbose_name="Orden componentes", null=True, blank=True)	# Orden en el que se selecionan los componentes
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
	aeronave 			= models.ForeignKey(Aeronave, null=True, blank=True, on_delete=models.CASCADE)
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
	descripcion		= RichTextField(verbose_name="Descripcion")
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