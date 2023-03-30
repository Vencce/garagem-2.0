from django.db import models
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)
    
    def _str_(self):
        return self.descricao
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)
    
    def _str_(self):
        return self.descricao

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Veículos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="Veículos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Veículos")
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    
    def _str_(self):
        return f"{self.marca}, {self.categoria}, {self.ano}, {self.cor}"
