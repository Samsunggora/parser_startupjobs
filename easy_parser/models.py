from django.db import models
from autoslug import AutoSlugField


class City(models.Model):
    name = models.CharField(max_length=170, unique=True)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'Citi'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Prof_language(models.Model):
    _name = models.CharField(max_length=170, unique=True)
    _slug = AutoSlugField(populate_from='_name')

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self._name


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    company = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Description')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='City')
    language = models.ForeignKey('Prof_language', on_delete=models.CASCADE, verbose_name='Language')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title
