from django.contrib import admin

from garagem.models import Categoria, Marca, Acessorio, Cor

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Cor)