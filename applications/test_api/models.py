from django.db import models

from .managers import PersonManager, PetManager


class Person(models.Model):
    objects = PersonManager()
    first_name = models.CharField(
        max_length=64,
        verbose_name='имя',
        help_text='сюда имя писать надо, максимум 64 символа'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='фамилия',
        help_text='сюда фамилию писать надо, максимум 64 символа'
    )

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return self.full_name()

    class Meta:
        ordering = ['id']
        unique_together = ['first_name', 'last_name']
        verbose_name = 'человек'
        verbose_name_plural = 'люди'


class Pet(models.Model):
    objects = PetManager()
    name = models.CharField(verbose_name='имя', max_length=64)
    owner = models.ForeignKey(Person, verbose_name='хозяин', on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.name + " " + str(self.owner.id) + " " + self.owner.full_name()

    def __repr__(self):
        return self.name + " " + str(self.owner.id) + " " + self.owner.full_name()

    class Meta:
        ordering = ['owner_id', 'name']
        unique_together = ['name', 'owner']
        verbose_name = 'петомец'
        verbose_name_plural = 'петомцы'
