from django import forms
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
			'fechaFabricacion',
			'fechaVencimiento',
			'proveedor',
			'fechaingreso',
			'hUtilizado',
			'descripcion',
			'estado',
			'vUtilOpc',
			'vUtil',
			'hvUtil',		
			'hUtilizado',		
			'hDurg',
		]
		widgets = {
			'numSerie': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'nombre': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'marca': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fabricante': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaFabricacion': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'fechaVencimiento': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'proveedor': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaingreso': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'4'}),
			'estado': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'vUtilOpc': forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil': forms.DateInput(attrs={'class':'form-control form-control-sm datepicker'}),
			'hvUtil': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hDurg': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),

		}
		labels = {
			'numSerie': 'Numero de serie',
			'nombre': 'Nombre',
			'marca': 'Marca /P-N o Modelo',
			'fabricante': 'Fabricante',
			'fechaFabricacion': 'Fecha de fabricacion',
			'fechaVencimiento': 'Fecha de vencimiento',
			'proveedor': 'Proveedor',
			'fechaingreso': 'Fecha de instalacion',
			'hUtilizado': 'Horas utilizado',
			'descripcion': 'Descripcion',
			'estado': 'Estado',
			'vUtil': 'Vida util calendario',
			'hvUtil': 'Horas vida util',		
			'hUtilizado': 'Horas de uso',		
			'hDurg': 'Horas DURG',
		}

class ComponenteUpdateForm(forms.ModelForm):
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
			'hUtilizado',
			'descripcion',
			'estado',
			'vUtilOpc',
			'vUtil',
			'hvUtil',		
			'hUtilizado',		
			'hDurg',
		]
		widgets = {
			'numSerie': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'nombre': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'marca': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fabricante': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaFabricacion': forms.DateInput(attrs={'class':'datepicker form-control form-control-sm'}),
			'fechaVencimiento': forms.DateInput(attrs={'class':'form-control form-control-sm'}),
			'proveedor': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'fechaingreso': forms.DateInput(attrs={'class':'form-control form-control-sm'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'6'}),
			'estado': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'vUtilOpc': forms.Select(attrs={'class':'form-control form-control-sm'}),
			'vUtil': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
			'hvUtil': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hUtilizado': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'hDurg': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
			'vUtil': forms.TextInput(attrs={'class':'form-control form-control-sm'}),

		}
		labels = {
			'numSerie': 'Numero de serie',
			'nombre': 'Nombre',
			'marca': 'Marca /P-N o Modelo',
			'fabricante': 'Fabricante',
			'fechaFabricacion': 'Fecha de fabricacion',
			'fechaVencimiento': 'Fecha de vencimiento',
			'proveedor': 'Proveedor',
			'fechaingreso': 'Fecha de instalacion',
			'hUtilizado': 'Horas utilizado',
			'descripcion': 'Descripcion',
			'estado': 'Estado',
			'hvUtil': 'Horas vida util',		
			'hUtilizado': 'Horas de uso',		
			'hDurg': 'Horas DURG',
			'vUtil': 'Vida util',
		}		

# -- Aeronave -- #

class AeronaveCreateForm(forms.ModelForm):
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