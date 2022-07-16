from django.shortcuts import render
from django.views import View
from .models import Person


class PersonViewSet(View):
    def get(self, request):
        return render(request, 'person_list.html',
                      {
                          'objects': Person.objects.all(),
                      }
                      )


class PersonView(View):
    def get(self, request, pk):
        return render(request, 'person_detail.html',
                      {
                          'object': Person.objects.get(pk=pk),
                      }
                      )


class PersonPetsViewSet(View):
    def get(self, request, pk):
        return render(request, 'person_pets.html',
                      {
                          'objects': Person.objects.get(pk=pk).pets,
                      }
                      )


class PersonPetsView(View):
    def get(self, request, pk, pk_pet):
        return render(request, 'person_pets_detail.html',
                      {
                          'object': Person.objects.get(pk=pk).pets.get(pk=pk_pet),
                      }
                      )
