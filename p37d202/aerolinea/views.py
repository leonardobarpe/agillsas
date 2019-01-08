from django.shortcuts import render, get_object_or_404, redirect

from .models import Componente
from .models import Aeronave
from .models import Vuelo
from .models import Orden

from .forms import Componente_formulario

from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .forms import *

from openpyxl import Workbook
from django.http import HttpResponse


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from easy_pdf.views import PDFTemplateView


# Create your views here.

# class StaffRequiredMixin(object):
# 	# Mixin requerira que el usuario sea miembro del staff
# 	@method_decorator(staff_member_required)
# 	def dispatch(self, request, *args, **kwargs):
# 		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# -- Componentes -- #
class componenteListView(ListView):
	model =	Componente
	template_name = 'componente/componente_list.html'

class componenteDetailView(DetailView):
	model =	Componente
	template_name = 'componente/componente_detail.html'

class componenteCreateView(CreateView):
	model = Componente
	form_class = ComponenteCreateForm
	template_name = 'componente/componente_form.html'
	success_url = reverse_lazy('componente_list')

class componenteUpdateView(UpdateView):
    model = Componente
    template_name = 'componente/componente_update_form.html'
    fields = [
	'nombre',	
	'marca',	
	'fabricante',	
	'fechaFabricacion',
	'fechaVencimiento',	
	'proveedor',	
	'fechaingreso',
	'descripcion',
    ]
    def get_success_url(self):
    	return reverse_lazy('componente_detail', args=[self.object.id]) + '?ok'

class componenteDeleteView(DeleteView):
	model = Componente
	template_name = 'componente/componente_confirm_delete.html'
	success_url = reverse_lazy('componente_list')


def componenteDownExcel(request):

	componentes = Componente.objects.all()

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename="componentes.csv"'
	writer = csv.writer(response, delimiter=';')

	writer.writerow(['No. serie','Nombre', 'Marca'])

	for componente in componentes:
		writer.writerow([componente.numSerie, componente.nombre, componente.marca])

	return response


# **********************************************
def componente_lista(request):
	componentes = Componente.objects.all()
	return render(request, 'componente/componente_lista.html', {'componentes': componentes})

def componente_info(request, componente_id):
	componente = get_object_or_404(Componente, id=componente_id)
	return render(request, 'componente/componente_info.html', {'componente':componente})

def componente_nuevo(request):
	componente_form = Componente_formulario()
	if request.method == "POST":
		componente_form = Componente_formulario(data=request.POST)
		if componente_form.is_valid():
			numSerie			= request.POST.get('numSerie', '')
			nombre				= request.POST.get('nombre', '')
			marca				= request.POST.get('marca', '')
			fabricante			= request.POST.get('fabricante', '')
			fechaFabricacion	= request.POST.get('fechaFabricacion', '')
			fechaVencimiento	= request.POST.get('fechaVencimiento', '')
			proveedor			= request.POST.get('proveedor', '')
			fechaIngreso		= request.POST.get('fechaingreso', '')
			descripcion			= request.POST.get('descripcion', '')
			return redirect(reverse('componente_nuevo')+"?componeteCreado")
	return render(request, 'componente/componente_nuevo.html', {'componente_form':componente_form})


# -- Aeronaves -- #

class aeronaveListView(ListView):
	model =	Aeronave
	template_name = 'aeronave/aeronave_list.html'

class aeronaveDetailView(DetailView):
	model =	Aeronave
	template_name = 'aeronave/aeronave_detail.html'

class aeronaveCreateView(CreateView):
	model = Aeronave
	template_name = 'aeronave/aeronave_form.html'
	fields = [
	'placa',	
	'marca',	
	'modelo',	
	'tipo',	
	'descripcion',
	'imagen',	
	'hVuelo',	
	'componente',
	]
	success_url = reverse_lazy('aeronave_list')

class aeronaveUpdateView(UpdateView):
    model = Aeronave
    template_name = 'aeronave/aeronave_update_form.html'
    fields = [
	'marca',	
	'modelo',	
	'tipo',	
	'descripcion',
	'imagen',	
	'componente',
    ]
    def get_success_url(self):
    	return reverse_lazy('aeronave_detail', args=[self.object.id])+ '?ok'

class aeronaveDeleteView(DeleteView):
	model = Aeronave
	template_name = 'aeronave/aeoronave_confirm_delete.html'
	success_url = reverse_lazy('aeronave_list')

def aeronaveDownExcel(request):
	aeronaves = Aeronave.objects.all()

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename="aeronaves.csv"'
	writer = csv.writer(response, delimiter=';')
	
	writer.writerow(['Placa','Marca', 'Modelo', 'Componente(s)'])

	for aeronave in aeronaves:
		writer.writerow([aeronave.placa, aeronave.marca, aeronave.modelo, aeronave.componente])

	return response

class aeronaveReporteExcel(TemplateView):
	def get(self, request, *args, **kwargs):
		aeronaves = Aeronave.objects.all()

		wb = Workbook()
		ws = wb.active
		ws['A1'] = 'REPORTE DE AERONAVES - DETALLES DE COMPONENTE'

		
		ws['A3'] = 'NO. SERIE'
		ws['A4'] = 'MARCA'
		ws['A5'] = 'PLACA'
		# ws['A7'] = 'COMPONENTES'
		# ws['A8'] = 'Nombre'
		# ws['B8'] = 'No. Serie'
		# ws['C8'] = 'Marca'
		# ws['D8'] = 'H. Util'
		# ws['E8'] = 'H. Utilizado'
		# ws['F8'] = 'H. Remanente'

		cont = 2
		for aeronave in aeronaves:
			ws.cell(row = 3, column = cont).value = aeronave.id
			ws.cell(row = 4, column = cont).value = aeronave.marca
			ws.cell(row = 5, column = cont).value = aeronave.placa
			cont+=1
			# for componente in aeronave.componente.all():
			# 	ws.cell(row = 9, column = 1).value = componente.nombre
			# 	ws.cell(row = 9, column = 2).value = componente.numSerie
			# 	ws.cell(row = 9, column = 3).value = componente.marca
			# 	ws.cell(row = 9, column = 4).value = componente.hvUtil
			# 	ws.cell(row = 9, column = 5).value = componente.hUtilizado
			# 	ws.cell(row = 9, column = 6).value = componente.horasRemanentes()



		nombre_archivo = 'aeronaveReporteExcel.xlsx'
		response = HttpResponse(content_type = "applications/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)

		return response

class aeronavePDFListView(PDFTemplateView):
	template_name = 'aeronave/pdf_aeronave_list.html'

# ***************************
def aeronave_lista(request):
	aeronaves = Aeronave.objects.all()
	return render(request, 'aeronave/aeronave_lista.html', {'aeronaves':aeronaves})

def aeronave_info(request, aeronave_id):
	aeronave = get_object_or_404(Aeronave, id=aeronave_id)
	return render(request, 'aeronave/aeronave_info.html',{'aeronave':aeronave})

# -- Vuelos -- #

class vueloListView(ListView):
	model =	Vuelo
	template_name = 'vuelo/vuelo_list.html' 

class vueloDetailView(DetailView):
	model =	Vuelo
	template_name = 'vuelo/vuelo_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class vueloCreateView(CreateView):
	model = Vuelo
	form_class = VueloCreateForm
	template_name = 'vuelo/vuelo_form.html'
	
	def form_valid(self, form):
		self.object = form.save(self)
		if self.object:
			horas = self.object.horas
			minutos = self.object.minutos
			for component in self.object.aeronave.componente.all():
				component.hUtilizado += horas
				component.mUtilizado += minutos
				component.hDurg += horas
				component.save()
			return super(vueloCreateView, self).form_valid(form)
		else:
			return self
	success_url = reverse_lazy('vuelo_list')


class vueloUpdateView(UpdateView):
    model = Vuelo
    template_name = 'vuelo/vuelo_update_form.html'
    fields = [
	'origen',
	'destino',
	'horas',
	'observaciones',
    ]
    def get_success_url(self):
    	return reverse_lazy('vuelo_detail', args=[self.object.id]) + '?ok'

class vueloDeleteView(DeleteView):
	model = Vuelo
	template_name = 'vuelo/vuelo_confirm_delete.html'
	success_url = reverse_lazy('vuelo_list')

# -- Orden -- #

class ordenListView(ListView):
	model =	Orden
	template_name = 'orden/orden_list.html'

class ordenDetailView(DetailView):
	model =	Orden
	template_name = 'orden/orden_detail.html'

class ordenCreateView(CreateView):
	model = Orden
	form_class = OrdenCreateForm
	template_name = 'orden/orden_form.html'

	def form_valid(self, form):
		self.object = form.save(self)
		if self.object:
			for component in self.object.componente.all():
				component.hDurg = 0
				component.save()
			return super(ordenCreateView, self).form_valid(form)
		else:
			return self
	success_url = reverse_lazy('orden_list')

class ordenUpdateView(UpdateView):
	model = Orden
	form_class = OrdenUpdateForm
	template_name = 'orden/orden_update_form.html'
	def get_success_url(self):
		return reverse_lazy('orden_detail', args=[self.object.id]) + '?ok'

class ordenDeleteView(DeleteView):
	model = Orden
	template_name = 'orden/orden_confirm_delete.html'
	success_url = reverse_lazy('orden_list')

class ordenPDFListView(PDFTemplateView):
	template_name = 'orden/pdf_orden_list.html'