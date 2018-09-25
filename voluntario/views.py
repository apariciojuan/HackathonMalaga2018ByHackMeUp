from django.shortcuts import render

from django.views.generic import (ListView, CreateView, DeleteView,
                                    UpdateView, DetailView)
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SearchForm, PersonCreateForm, DiasDisponiblesCreateForm

from .models import Person, DiasDisponibles
# Create your views here.

class HomeList(ListView):
    model = Person
#    paginate_by = 20
#    fields = ['titulo', 'contenido', 'categoria', 'slug']
    form_class = SearchForm
    #context_object_name = 'object_list1'
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
            print(datos)
            filterRecive = datos['Disponibilidad']
            filterRecive2 = datos['Ciudades']
            if 'All' in filterRecive:
                return HttpResponseRedirect('/')
            if filterRecive != []: #si el formulario NO esta vacio
                #queryset = Person.objects.filter(
                #                            disponibilidad__in=filterRecive)
                queryset = DiasDisponibles.objects.filter()
                ee = Person.objects.all()
                gg = ee[0].disponibilidad
                rr = gg.Lunes.all()
                tt = rr[0].to
                print(tt)
            else:
                queryset = Person.objects.all()
            if filterRecive2 != []:
                    queryset = queryset.filter(ciudad__in=filterRecive2)
        else:
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
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
