from django.contrib import admin

from garagem.models import Categoria, Marca, Acessorio, Cor, Veiculo, Modelo

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Veiculo)
admin.site.register(Modelo)