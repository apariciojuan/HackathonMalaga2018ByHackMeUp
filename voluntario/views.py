from django.shortcuts import render

from django.views.generic import (ListView, CreateView, DeleteView,
                                    UpdateView, DetailView)
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SearchForm, PersonCreateForm, DiasDisponiblesCreateForm

from .models import Person, DiasDisponibles
# Create your views here.

class HomeList(ListView):
    model = Person
#    paginate_by = 2
    form_class = SearchForm
    template_name = 'home_list.html'

    def get_context_data(self, **kwargs):
        context =super(HomeList, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

def PersonListFilter(request):
    #Vista para el filtro
    form = SearchForm
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid(): #si el formulario en valido
            datos = form.cleaned_data
            filterRecive = datos['Disponibilidad']
            filterRecive2 = datos['Ciudades']
            if 'All' in filterRecive:
                return HttpResponseRedirect('/')
            #filtramos ciudades primero si hay y luego por dias
            if filterRecive2 != []:
                queryset = Person.objects.filter(ciudad__in=filterRecive2)
            if filterRecive != []:
                if filterRecive2 != []: #si el formulario NO esta vacio
                    usuarios = queryset
                else:
                    usuarios = Person.objects.all()
                queryset= []
                cantidad  = usuarios.count()
                for x in range(0,cantidad):
                    for y in filterRecive:
                        if 'Lunes' == y:
                            if (usuarios[x].disponibilidad.Lunes.all().count() != 0
                                    and usuarios[x].disponibilidad.Lunes.all()[0].to != '--'):
                                queryset.append(usuarios[x])
                        elif 'Martes' == y:
                            if (usuarios[x].disponibilidad.Martes.all().count() != 0
                                    and usuarios[x].disponibilidad.Martes.all()[0].to != '--'):
                                queryset.append(usuarios[x])
                        elif 'Miercoles' == y:
                            if (usuarios[x].disponibilidad.Miercoles.all().count() != 0
                                    and usuarios[x].disponibilidad.Miercoles.all()[0].to != '--'):
                                queryset.append(usuarios[x])
                        elif 'Jueves' == y:
                            if (usuarios[x].disponibilidad.Jueves.all().count() != 0
                                    and usuarios[x].disponibilidad.Jueves.all()[0].to != '--'):
                                queryset.append(usuarios[x])
                        elif 'Viernes' == y:
                            if (usuarios[x].disponibilidad.Viernes.all().count() != 0
                                    and usuarios[x].disponibilidad.Viernes.all()[0].to != '--'):
                                queryset.append(usuarios[x])
                        elif 'Sabado' == y:
                            if (usuarios[x].disponibilidad.Sabado.all().count() != 0
                                    and usuarios[x].disponibilidad.Sabado.all()[0].to != '--'):
                                queryset.append(usuarios[x])
                        elif 'Domingo' == y:
                            if (usuarios[x].disponibilidad.Domingo.all().count() !=0
                                    and usuarios[x].disponibilidad.Domingo.all()[0].to != '--'):
                                queryset.append(usuarios[x])
            else:
                if filterRecive2 == [] and filterRecive == []:
                #si no hay filtro o es todo manda todo
                    queryset = Person.objects.all()
        else:
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        return HttpResponseRedirect('/')
#esta parte es para la paginacion manteniendo el filtro queda para otra version
#hay que mantener los filtros para paginar, sacamos el return de arriba
        filterRecive = request.GET.get('filtro')
        #recive por get en string asi lo cambio a lista
        import ast; filterRecive = ast.literal_eval(filterRecive)
        queryset = Articles.objects.filter(disponibilidad__in=filterRecive)
    else:
        return HttpResponseRedirect('/')
    ctx = {'form': form, 'object_list': queryset,
           'objectFilter': filterRecive}
    return render(request, 'home_list.html', ctx)



class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    template_name = 'crear_persona.html'
    form_class = PersonCreateForm
    second_form_class = DiasDisponiblesCreateForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context =super(PersonCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid():
            datosVoluntario = form.save(commit=False)
            datosVoluntario.disponibilidad = form2.save()
            datosVoluntario.save()
        return HttpResponseRedirect('/')


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    template_name = 'update_persona.html'
    form_class = PersonCreateForm
    second_form_class = DiasDisponiblesCreateForm
    success_url = reverse_lazy('voluntario:home')

    def get_context_data(self, **kwargs):
        context =super(PersonUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        persona = self.model.objects.get(id=pk)
        dias = DiasDisponibles.objects.get(id=persona.disponibilidad_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        #para que muestre los datos cargados es el instance
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=dias)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_person = kwargs['pk']
        persona = self.model.objects.get(id=id_person)
        form = self.form_class(request.POST, instance=persona)

        dias = DiasDisponibles.objects.get(id=persona.disponibilidad_id)
        form2 = self.second_form_class(request.POST, instance=dias)
        if form.is_valid():
            datosVoluntario = form.save(commit=False)
            datosVoluntario.disponibilidad = form2.save()
            datosVoluntario.save()

        return HttpResponseRedirect('/')


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('voluntario:home')


class PersonVer(DetailView):
    model = Person
    template_name = 'ver_persona.html'

""" Falta mandar mensaje cuando la busque no da resultados sino queda vacio,
    paginar en el listView y en el filter, agregar una forma que cuando se
    agregue un voluntario o se actualize se puede agregar mas rangos horarios
    y solo desde el admin esto.
    Asi como esta cubre los requisitos del Hackethon Malaga 2018 de HackMeUp.
"""
