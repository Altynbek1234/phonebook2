from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView

from . import forms, models
from .models import Person, PhoneNumber


# def search(request):
#     queryset = Person.objects.all()
#     query = request.GET.get('q')
#     if query:
#         queryset = queryset.filter(
#             Q(name__icontains=query) |
#             Q(phone__icontains=query)
#         ).distinct()
#     context = {
#         'queryset': queryset
#     }
#     return render(request, 'search_results.html', context)

# class Search(ListView):
#     template_name = 'search_results.html'
#     def get_queryset(self):
#         return Person.objects.filter(name__icontains=self.request.GET.get("q"))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["q"]=self.request.GET.get("q")
#         return context

class SearchResultsView(ListView):
    model = Person
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

# class HomePageView(TemplateView):
#     template_name = 'home.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['persons'] = models.Person.objects.all()
#         return context

def posts_list(request):
    persons = Person.objects.all()
    paginator = Paginator(persons, 2)
    page_number = request.GET.get('page',1)

    page = paginator.get_page(page_number)
    return render(request, 'home.html', context={'persons': page})

class AddPhoneFormView(CreateView):
    template_name = 'add.html'
    form_class = forms.CreatePersonForm
    success_url = reverse_lazy('home')
    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.PhoneNumber.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()

class DeletePersonView(DeleteView):
    model = models.Person
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

# class UpdatePersonView(UpdateView):
#     model = Person
#     template_name = 'update.html'
#     form_class = forms.UpdatePersonForm
#     success_url = reverse_lazy('home')
#
#
#     def get_success_url(self) -> str:
#         phone_numbers = self.request.POST.get('name')
#         print(phone_numbers)
#         for phone_number in phone_numbers:
#             models.PhoneNumber.objects.update(phone=phone_number, contact=self.object)
#         return super().get_success_url()
class UpdatePersonView(UpdateView):
    model = Person #model
    model = PhoneNumber
    fields = '__all__' # fields / if you want to select all fields, use "__all__"
    template_name = 'update.html' # templete for updating
    success_url = reverse_lazy('home')

