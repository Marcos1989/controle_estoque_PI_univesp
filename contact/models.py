from django.db import models

class Contact(models.Model):
    Descricao = models.CharField(max_length=255)
    Tamanho_Roupas = (("PP", "PP"),("P", "P"),("M", "M"),("G", "G"),("GG", "GG"),("EXG", "EXG"),("G1", "G1"),("G2", "G2"),("G3", "G3"))
    Tamanho = models.CharField(max_length=4,choices=Tamanho_Roupas)
    Estoque_entrada = models.CharField(max_length=255)
    Codigo_Produto = models.CharField(max_length=255)
    Preço_Compra = models.CharField(max_length=255)
    Preço_Venda = models.CharField(max_length=255)

    def __str__(self):
        return self.Descricao