from django.shortcuts import render

from django.views.generic import (ListView, CreateView, DeleteView,
                                    UpdateView, DetailView)

from django.http import HttpResponseRedirect, HttpResponse


from .forms import SearchForm

from .models import Person
# Create your views here.

def home(request):
    return HttpResponse("hola mundo")

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
                return HttpResponseRedirect('/homeView/')
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
            return HttpResponseRedirect('/homeView/')
    elif request.method == 'GET':
        filterRecive = request.GET.get('filtro')
        #recive por get en string asi lo cambio a lista
        import ast; filterRecive = ast.literal_eval(filterRecive)
        queryset = Articles.objects.filter(disponibilidad__in=filterRecive)
    else:
        return HttpResponseRedirect('/homeView/')

    ctx = {'form': form, 'object_list': queryset,
           'objectFilter': filterRecive}
    return render(request, 'home_list.html', ctx)


