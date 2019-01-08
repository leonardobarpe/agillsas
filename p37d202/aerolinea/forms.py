from django import forms

from .models import *

# -- Componente -- #
class ComponenteCreateForm(forms.ModelForm):
	class Meta:
		model = Componente
		fields = [
			'numSerie',
			'nombre',
			'marca',
			'fabricante',
			'fechaFabricacion',
			'fechaVencimiento',
			'proveedor',
			'fechaingreso',
			'descripcion'
		]
		widgets = {
			'numSerie': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'nombre': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'marca': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fabricante': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaFabricacion': forms.DateInput(attrs={'class':'form-control form-control-sm','type':'date'}),
			'fechaVencimiento': forms.DateInput(attrs={'class':'form-control form-control-sm','type':'date'}),
			'proveedor': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaingreso': forms.DateInput(attrs={'class':'form-control form-control-sm','type':'date'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
		}
		labels = {
			'numSerie': 'Numero de serie',
			'nombre': 'Nombre',
			'marca': 'Marca',
			'fabricante': 'Fabricante',
			'fechaFabricacion': 'Fecha de fabricacion',
			'fechaVencimiento': 'Fecha de vencimiento',
			'proveedor': 'Proveedor',
			'fechaingreso': 'Fecha de ingreso',
			'descripcion': 'Descripcion',
		}		

	# numSerie			= models.CharField(max_length=200, verbose_name="Numero de Serie")					# numero de serie del componente
	# nombre				= models.CharField(max_length=200, verbose_name="Nombre")							# nombre del componente
	# marca				= models.CharField(max_length=200, verbose_name="Marca")							# marca /P-N o Model del componente
	# fabricante			= models.CharField(max_length=200, verbose_name="Fabricante")						# fabricante del componente
	# fechaFabricacion	= models.DateField(verbose_name="Fecha de Fabricacion")								# fecha de fabricacion del componente 
	# fechaVencimiento	= models.DateField(verbose_name="Fecha de Vencimiento")								# fecha de vencimineto del componente
	# proveedor			= models.CharField(max_length=200, verbose_name="Proveedor")						# proveedor del componente
	# fechaingreso		= models.DateField(verbose_name="Fecha de Ingreso")									# fecha de ingreso del componente
	# descripcion			= RichTextField(verbose_name="Descripcion")											# descripcion del componente
	# hvUtil 				= models.IntegerField(verbose_name="Horas de vida util",null=True, blank=True)		# horas de vida util
	# mvUtil 				= models.IntegerField(verbose_name="Minutos de vida util",null=True, blank=True)	# minutos de vida util
	# hUtilizado			= models.IntegerField(verbose_name="Horas utilizado",null=True, blank=True)			# horas utilizado
	# mUtilizado			= models.IntegerField(verbose_name="Minutos utilizado",null=True, blank=True)		# minutos utilizado
	# hDurg				= models.IntegerField(verbose_name="Horas Durg",null=True, blank=True)				# horas durg
	# mDurg				= models.IntegerField(verbose_name="Minutos Durg",null=True, blank=True)			# minutos durg
	# hRemanente			= models.IntegerField(verbose_name="Horas Remanente",null=True, blank=True)			# horas remanete
	# mRemanente			= models.IntegerField(verbose_name="Minutos Remanente",null=True, blank=True)		# minutos remanete	
	# estado				= models.CharField(max_length=200, verbose_name="Estado")							# estado del componente (bodega, instalado, baja)




class VueloCreateForm(forms.ModelForm):
	class Meta:
		model = Vuelo
		fields = [
			'fecha',
			'origen',
			'destino',
			'horas',
			'minutos',
			'observaciones',
			'aeronave',
		]
		widgets = {
			'fecha': forms.DateInput(attrs={'class':'form-control form-control-sm','type':'date'}),
			'origen': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'destino': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'horas': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'minutos': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'observaciones': forms.Textarea(attrs={'class':'form-control form-control-sm'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm','type':'date'}),
		}
		labels = {

		}


# class Vuelo(models.Model):
# 	fecha				= models.DateField(verbose_name="Fecha de vuelo")									# Fecha del vuelo
# 	origen				= models.CharField(max_length=200, verbose_name="Origen")							# Sitio de origen del vuelo
# 	destino				= models.CharField(max_length=200, verbose_name="Destino")							# Sitio de destino del vuelo
# 	horas				= models.CharField(max_length=200, verbose_name="Horas de vuelo", null=True)		# Horas de vuelo
# 	minutos				= models.CharField(max_length=200, verbose_name="Minutos de vuelo", null=True)		# minutos de vuelo
# 	observaciones		= models.TextField(verbose_name="Observaciones", null=True)							# Observaciones del vuelo
# 	# -- Auditoria -- #
# 	creado				= models.DateTimeField(auto_now_add = True,null=True, blank=True)					# Registra fecha al crearlo
# 	actualizado			= models.DateTimeField(auto_now = True)												# Registra fecha al crearlo
# 	# -- Llaves --#
# 	aeronave 			= models.ForeignKey(Aeronave, null=True, blank=True, on_delete=models.CASCADE)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class OrdenCreateForm(forms.ModelForm):
	class Meta:
		model = Orden
		fields = [
			'ciudad',
			'fecha',
			'descripcion',
			'tecnico',
			'dirCC',
			'aeronave',
			'componente',
		]
		widgets = {
			'ciudad': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fecha': forms.DateInput(attrs={'class':'form-control form-control-sm','type':'date'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm'}),
			'tecnico': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'dirCC':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm'}),
			'componente':forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),
		}
		labels = {
			'ciudad':'Ciudad',
			'fecha':'Fecha',
			'descripcion':'Descripcion',
			'tecnico':'Tecnico',
			'dirCC':'Director control de calidad',
			'aeronave':'Aeronave',
			'componente':'Componente(s)',
		}

class OrdenUpdateForm(forms.ModelForm):
	class Meta:
		model = Orden
		fields = [
			'ciudad',
			'fecha',
			'descripcion',
			'tecnico',
			'dirCC',
			'aeronave',
			'componente',
		]
		widgets = {
			'ciudad': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fecha': forms.DateInput(attrs={'class':'form-control form-control-sm','type':'date'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm'}),
			'tecnico': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'dirCC':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm'}),
			'componente':forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),
		}
		labels = {
			'ciudad':'Ciudad',
			'fecha':'Fecha',
			'descripcion':'Descripcion',
			'tecnico':'Tecnico',
			'dirCC':'Director control de calidad',
			'aeronave':'Aeronave',
			'componente':'Componente(s)',
		}


	# ciudad			= models.CharField(max_length=200, verbose_name="Ciudad")
	# fecha 			= models.DateField(verbose_name="Fecha de Orden")
	# descripcion		= models.TextField(verbose_name="Descripcion", null=True, blank=True)
	# tecnico			= models.CharField(max_length=200, verbose_name="Tecnico")
	# dirCC			= models.CharField(max_length=200, verbose_name="Director control calidad")
	# # -- Auditoria -- #
	# creado				= models.DateTimeField(auto_now_add = True,null=True, blank=True)
	# actualizado			= models.DateTimeField(auto_now = True)	
	# # -- Llaves --#
	# aeronave 		= models.ForeignKey(Aeronave, verbose_name="Aeronave", on_delete=models.CASCADE)
	# componente		= models.ManyToManyField(Componente, blank=True, verbose_name="Componente(s)")





# ***********************************************************************************
class Componente_formulario(forms.Form):
	numSerie			= forms.CharField(label="Numero de Serie", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	nombre				= forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	marca				= forms.CharField(label="Marca", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	fabricante			= forms.CharField(label="Fabricante", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	fechaFabricacion	= forms.DateField(label="Fecha de Fabricacion", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA'}))
	fechaVencimiento	= forms.DateField(label="Fecha de Vencimiento", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA'}))
	proveedor			= forms.CharField(label="Proveedor", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	fechaIngreso		= forms.DateField(label="Fecha de Ingreso", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA'}))
	descripcion			= forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))