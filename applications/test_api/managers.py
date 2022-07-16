from django.db import models
from django.db.models import Count


class PersonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class PetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def have_friends(self, flag):
        if flag:
            return self.get_queryset().annotate(pets_count=Count('owner__pets')).filter(pets_count__gte=2)
        else:
            return self.get_queryset().annotate(pets_count=Count('owner__pets')).filter(pets_count__lte=1)
