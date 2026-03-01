class Rota:
    def __init__(self, origem, destino, distancia_km, tipo_terreno="plano"):
        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km 
        self.tipo_terreno = tipo_terreno