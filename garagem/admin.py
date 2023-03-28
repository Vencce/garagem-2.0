from django.contrib import admin

from garagem.models import Categoria, Marca

admin.site.register(Marca)
admin.site.register(Categoria)