from django.contrib import admin

from garagem.models import Categoria, Marca, Acessorio, Cor, Veiculo

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Veiculo)