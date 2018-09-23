from django.shortcuts import render

from django.views.generic import (ListView, CreateView, DeleteView,
                                    UpdateView, DetailView)
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

#from django.contrib.auth.models import User

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SearchForm, PersonCreateForm

from .models import Person
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
            filterRecive3 = datos['Ocupacion']
            if 'All' in filterRecive:
                return HttpResponseRedirect('/')
            if filterRecive != []: #si el formulario NO esta vacio
                queryset = Person.objects.filter(
                                            disponibilidad__in=filterRecive)
            else:
                queryset = Person.objects.all()
            if filterRecive3 != []:
                    queryset = queryset.filter(ocupacion__in=filterRecive3)
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



class PersonCreate(CreateView):
    model = Person
    template_name = 'crear_persona.html'
    form_class = PersonCreateForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context =super(PersonCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            articulo = form.save()
        return HttpResponseRedirect('/')


class PersonUpdate(UpdateView):
    model = Person
    template_name = 'update_persona.html'
    form_class = PersonCreateForm
    success_url = reverse_lazy('voluntario:home')

    def get_context_data(self, **kwargs):
        context =super(PersonUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        persona = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_person = kwargs['pk']
        persona = self.model.objects.get(id=id_person)
        form = self.form_class(request.POST, instance=persona)
        print(form)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('voluntario:home')


class PersonVer(DetailView):
    model = Person
    template_name = 'ver_persona.html'
