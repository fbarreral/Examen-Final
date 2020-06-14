from django.shortcuts import render
from django.views.generic.list import ListView

from alumn.models import Alumn
from grade.models import Grade
from section.models import Section
from inscription.models import Inscription

def index(request):
    return render(request, 'index.html')


class AlumnListView(ListView):
    template_name = 'alumn.html'
    queryset = Alumn.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Alumnos'
        context['alumns'] =context['object_list']

        print(context)

        return context

class GradeListView(ListView):
    template_name = 'grade.html'
    queryset = Grade.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Grados'
        context['grades'] =context['object_list']

        print(context)

        return context

class SectionListView(ListView):
    template_name = 'section.html'
    queryset = Section.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Seccion'
        context['sections'] =context['object_list']

        print(context)

        return context

class InscriptionListView(ListView):
    template_name = 'inscription.html'
    queryset = Inscription.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Inscripciones'
        context['inscriptions'] =context['object_list']

        print(context)

        return context