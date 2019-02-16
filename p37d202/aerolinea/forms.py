from django import forms
from django.db.models import Count, Q
from ckeditor.widgets import CKEditorWidget

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
			# 'fechaFabricacion',
			'fechaVencimiento',
			'mesesVencimiento',
			'proveedor',
			'fechaingreso',
			'hUtilizado',
			'descripcion',
			# 'estado',
			'vUtilOpc',
			'vUtil',
			'hvUtil',		
			'hUtilizado',		
			'hDurg',
			'ordenTrabajo',
			
			'tipo',
			'vUtilOpc_i',
			'vUtil_i',
			'hvUtil_i',
			'vUtilOpc_p',
			'vUtil_p',
			'hvUtil_p',

		]
		widgets = {
			'numSerie': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'nombre': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'marca': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fabricante': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			# 'fechaFabricacion': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'fechaVencimiento': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'mesesVencimiento': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'proveedor': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaingreso': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'4'}),
			# 'estado': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'vUtilOpc': forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hDurg': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'ordenTrabajo': forms.TextInput(attrs={'class':'form-control form-control-sm'}),

			'tipo':forms.Select(attrs={'class':'form-control form-control-sm'}),
			
			'vUtilOpc_i':forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil_i':forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil_i':forms.NumberInput(attrs={'class':'form-control form-control-sm'}),

			'vUtilOpc_p':forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil_p':forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil_p':forms.NumberInput(attrs={'class':'form-control form-control-sm'}),				
# tipo				= models.CharField(max_length=20, verbose_name="Tipo componente", choices=opcTipo, default=tipo1, null=True)
# vUtilOpc_i			= models.CharField(max_length=20, verbose_name="TBO inspeccion inicial", choices=opcVutil_i, default=HORAS_i, null=True)
# vUtil_i				= models.DateField(verbose_name="TBO Calendario inspec inicial",null=True, blank=True)
# hvUtil_i			= models.IntegerField(verbose_name="Horas inspec inicial TBO",null=True, blank=True, default=1)	
# vUtilOpc_p			= models.CharField(max_length=20, verbose_name="TBO inspeccion posterior", choices=opcVutil_p, default=HORAS_p, null=True)
# vUtil_p				= models.DateField(verbose_name="TBO Calendario inspec posterior",null=True, blank=True)
# hvUtil_p			= models.IntegerField(verbose_name="Horas inspec posterior TBO",null=True, blank=True, default=1)	

		}
		labels = {
			'numSerie': 'Numero de serie',
			'nombre': 'Nombre',
			'marca': 'Parte/Numero',
			'fabricante': 'Fabricante',
			# 'fechaFabricacion': 'Fecha de fabricacion',
			'fechaVencimiento': 'Fecha de vencimiento',
			'mesesVencimiento': 'Meses de vencimiento',
			'proveedor': 'Proveedor',
			'fechaingreso': 'Fecha de instalacion',
			'hUtilizado': 'Horas total',
			'descripcion': 'Descripcion',
			# 'estado': 'Estado',
			'vUtil': 'TBO calendario',
			'hvUtil': 'Horas TBO',		
			'hUtilizado': 'Horas total',		
			'hDurg': 'Horas DURG',
			'ordenTrabajo': 'Orden de trabajo',

			'tipo':'Tipo componente',
			
			'vUtilOpc_i':'TBO inspec inicial',
			'vUtil_i':'TBO calendario inspec inicial',
			'hvUtil_i':'Horas TBO inspec inicial',

			'vUtilOpc_p':'TBO inspec posterior',
			'vUtil_p':'TBO calendario inspec posterior',
			'hvUtil_p':'Horas TBO inspec posterior',			
		}

class ComponenteUpdateForm(forms.ModelForm):
	class Meta:
		model = Componente
		fields = [
			'numSerie',
			'nombre',
			'marca',
			'fabricante',
			# 'fechaFabricacion',
			'fechaVencimiento',
			'mesesVencimiento',
			'proveedor',
			'fechaingreso',
			'hUtilizado',
			'descripcion',
			# 'estado',
			'vUtilOpc',
			'vUtil',
			'hvUtil',		
			'hUtilizado',		
			'hDurg',
			'ordenTrabajo',
			
			'tipo',
			'vUtilOpc_i',
			'vUtil_i',
			'hvUtil_i',
			'vUtilOpc_p',
			'vUtil_p',
			'hvUtil_p',

		]
		widgets = {
			'numSerie': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'nombre': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'marca': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fabricante': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			# 'fechaFabricacion': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'fechaVencimiento': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'mesesVencimiento': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'proveedor': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaingreso': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'4'}),
			# 'estado': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'vUtilOpc': forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hDurg': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'ordenTrabajo': forms.TextInput(attrs={'class':'form-control form-control-sm'}),

			'tipo':forms.Select(attrs={'class':'form-control form-control-sm'}),
			
			'vUtilOpc_i':forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil_i':forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil_i':forms.NumberInput(attrs={'class':'form-control form-control-sm'}),

			'vUtilOpc_p':forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil_p':forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil_p':forms.NumberInput(attrs={'class':'form-control form-control-sm'}),				
# tipo				= models.CharField(max_length=20, verbose_name="Tipo componente", choices=opcTipo, default=tipo1, null=True)
# vUtilOpc_i			= models.CharField(max_length=20, verbose_name="TBO inspeccion inicial", choices=opcVutil_i, default=HORAS_i, null=True)
# vUtil_i				= models.DateField(verbose_name="TBO Calendario inspec inicial",null=True, blank=True)
# hvUtil_i			= models.IntegerField(verbose_name="Horas inspec inicial TBO",null=True, blank=True, default=1)	
# vUtilOpc_p			= models.CharField(max_length=20, verbose_name="TBO inspeccion posterior", choices=opcVutil_p, default=HORAS_p, null=True)
# vUtil_p				= models.DateField(verbose_name="TBO Calendario inspec posterior",null=True, blank=True)
# hvUtil_p			= models.IntegerField(verbose_name="Horas inspec posterior TBO",null=True, blank=True, default=1)	

		}
		labels = {
			'numSerie': 'Numero de serie',
			'nombre': 'Nombre',
			'marca': 'Parte/Numero',
			'fabricante': 'Fabricante',
			# 'fechaFabricacion': 'Fecha de fabricacion',
			'fechaVencimiento': 'Fecha de vencimiento',
			'mesesVencimiento': 'Meses de vencimiento',
			'proveedor': 'Proveedor',
			'fechaingreso': 'Fecha de instalacion',
			'hUtilizado': 'Horas total',
			'descripcion': 'Descripcion',
			# 'estado': 'Estado',
			'vUtil': 'TBO calendario',
			'hvUtil': 'Horas TBO',		
			'hUtilizado': 'Horas total',		
			'hDurg': 'Horas DURG',
			'ordenTrabajo': 'Orden de trabajo',

			'tipo':'Tipo componente',
			
			'vUtilOpc_i':'TBO inspec inicial',
			'vUtil_i':'TBO calendario inspec inicial',
			'hvUtil_i':'Horas TBO inspec inicial',

			'vUtilOpc_p':'TBO inspec posterior',
			'vUtil_p':'TBO calendario inspec posterior',
			'hvUtil_p':'Horas TBO inspec posterior',			
		}

# -- Aeronave -- #

class AeronaveCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AeronaveCreateForm, self).__init__(*args, **kwargs)
		self.fields['componente'].queryset=Componente.objects.annotate(aeronaves=Count("aeronave")).filter(aeronaves__lte=0)

	class Meta:
		model = Aeronave
		fields = [
			'placa',				
			'marca',				
			'modelo',				
			'tipo',				
			'descripcion',			
			'hVuelo',				
			'componente',
		]
		widgets = {
			'placa':		forms.TextInput(attrs={'class':'form-control form-control-sm'}),				
			'marca': 		forms.TextInput(attrs={'class':'form-control form-control-sm'}),		
			'modelo': 		forms.TextInput(attrs={'class':'form-control form-control-sm'}),		
			'tipo': 		forms.TextInput(attrs={'class':'form-control form-control-sm'}),		
			'descripcion': 	forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),		
			'hVuelo': 		forms.NumberInput(attrs={'class':'form-control form-control-sm'}),		
			'componente':	forms.SelectMultiple(attrs={'class':'form-control form-control-sm chosen-select ','data-placeholder': 'Click sobre el campo para agregar componente(s)'}),
		}
		labels = {
			'placa':		'Matricula',
			'marca': 		'Marca',
			'modelo': 		'Modelo',
			'tipo': 		'Tipo',
			'descripcion': 	'Descripcion',
			'hVuelo': 		'Horas de vuelo',
			'componente':	'Componentes',
		}

class AeronaveUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AeronaveUpdateForm, self).__init__(*args, **kwargs)
		self.fields['componente'].queryset=Componente.objects.annotate(aeronaves=Count("aeronave")).filter(Q(aeronaves__lte=0)|Q(aeronave=self.instance))

	class Meta:
		model = Aeronave
		fields = [
			'placa',				
			'marca',				
			'modelo',				
			'tipo',				
			'descripcion',			
			'hVuelo',	
			'componente',
		]
		widgets = {
			'placa':		forms.TextInput(attrs={'class':'form-control form-control-sm'}),				
			'marca': 		forms.TextInput(attrs={'class':'form-control form-control-sm'}),		
			'modelo': 		forms.TextInput(attrs={'class':'form-control form-control-sm'}),		
			'tipo': 		forms.TextInput(attrs={'class':'form-control form-control-sm'}),		
			'descripcion': 	forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),		
			'hVuelo': 		forms.NumberInput(attrs={'class':'form-control form-control-sm'}),		
			'componente':	forms.SelectMultiple(attrs={'class':'chosen-select','data-placeholder': 'Click sobre el campo para agregar componente(s)'}),
		}
		labels = {
			'placa':		'Matricula',
			'marca': 		'Marca',
			'modelo': 		'Modelo',
			'tipo': 		'Tipo',
			'descripcion': 	'Descripcion',
			'hVuelo': 		'Horas de vuelo',
			'componente':	'Componentes',
		}

# -- Vuelo -- #

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
			'fecha': forms.DateInput(attrs={'class':'datepicker form-control form-control-sm'}),
			'origen': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'destino': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'horas': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'minutos': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'observaciones': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm chosen-select '}),
		}
		labels = {
			'fecha':			'Fecha',
			'origen':			'Origen', 
			'destino':			'Destino', 
			'horas':			'Horas', 
			'minutos':			'Minutos', 
			'observaciones':	'Observaciones', 
			'aeronave':			'Aeronave', 
		}

class VueloUpdateForm(forms.ModelForm):
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
			'fecha': forms.DateInput(attrs={'class':'datepicker form-control form-control-sm'}),
			'origen': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'destino': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'horas': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'minutos': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'observaciones': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm chosen-select '}),
		}
		labels = {
			'fecha':			'Fecha',
			'origen':			'Origen', 
			'destino':			'Destino', 
			'horas':			'Horas', 
			'minutos':			'Minutos', 
			'observaciones':	'Observaciones', 
			'aeronave':			'Aeronave', 
		}		
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
			'fecha': forms.DateInput(attrs={'class':'datepicker form-control form-control-sm'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),
			'tecnico': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'dirCC':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm chosen-select'}),
			'componente':forms.SelectMultiple(attrs={'class':'chosen-select'}),
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
			'fecha': forms.DateInput(attrs={'class':'datepicker form-control form-control-sm'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),
			'tecnico': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'dirCC':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'aeronave': forms.Select(attrs={'class':'form-control form-control-sm chosen-select'}),
			'componente':forms.SelectMultiple(attrs={'class':'chosen-select'}),
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