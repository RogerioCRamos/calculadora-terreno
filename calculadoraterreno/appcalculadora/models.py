from django.db import models

class PlanoUrbano(models.Model):
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    link_plano_diretor = models.CharField()
    zona_urbana = models.CharField(max_length=50)
    frente_terreno = models.IntegerField()
    profundidade_terreno = models.IntegerField()
    area_terreno = models.IntegerField()
    ca_basico = models.IntegerField()
    ca_maximo = models.IntegerField()
    taxa_ocupacao = models.IntegerField()
    recuo_frontal = models.IntegerField()
    recuo_lateral = models.IntegerField()
    recuo_fundos = models.IntegerField()
    altura_maxima = models.IntegerField()
    studio_m2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dois_dorm_m2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tres_dorm_m2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    percentual_area_comum = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vagas_minimas_unidade = models.IntegerField(null=True, blank=True)
    
    comercio_obrigatorio = models.CharField(
        max_length=3,
        choices=[('Sim', 'Sim'), ('Não', 'Não')],
        default='Não'
    )