from django.contrib import admin
from .models import *

# Register your models here.
class ComponenteAdmin(admin.ModelAdmin):
	readonly_fields = ('creado', 'actualizado')
	list_display = ('numSerie', 'nombre', 'marca', 'creado')
	ordering = ('-creado', 'nombre')
	search_fields = ('numSerie', 'nombre')   # PAra busqueda de campos de llaves foraneas se pone el nombre del modelo __ y el nombre del campo
	date_hierarchy = 'creado'				# permite navegar entre fechas
	# list_filter = ()						# por las llaves foraneas
	# Inyectamos nuestro fichero css
	class Media:
		css = {
		'all': ('core/css/custom_ckeditor.css',)
		}
        
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Aeronave)
admin.site.register(Vuelo)
admin.site.register(Orden)
admin.site.register(Cumplimiento)
admin.site.register(ItemCumplimiento)