class Trem:
    def __init__(self, id_trem, tipo_carga, capacidade, velocidade_maxima):
        self.id_trem = id_trem
        self.tipo_carga = tipo_carga
        self.capacidade = capacidade # em toneladas
        self.velocidade_maxima = velocidade_maxima # em km/h
        self.status = "parado" 
        self.carga_atual = 0
        self.posicao_km = 0
        self.horas_viagem = 0
        self.atraso_total = 0
        self.rota = None
    
    def carregar(self, toneladas):
        if toneladas <= self.capacidade:
            self.carga_atual = toneladas
        else:
            raise ValueError(f"Trem {self.id_trem} não pode carregar mais que sua capacidade de {self.capacidade} toneladas.")
    
    def iniciar_viagem(self, rota):
        if self.carga_atual > 0:
            self.status = "em viagem"
            self.rota = rota
            self.posicao_km = 0
            self.velocidade_atual = 0
        else:
            raise ValueError(f"Trem {self.id_trem} não pode iniciar a viagem sem carga.") 

    def calcular_velocidade_real(self):
        #penalidade por peso
        fator_peso = 1 - (self.carga_atual / self.capacidade) * 0.3

        #penalidade por tipo de terreno
        if self.rota.tipo_terreno == "serra":
            fator_terreno = 0.7
        else: 
            fator_terreno = 1

        velocidade = self.velocidade_maxima * fator_peso * fator_terreno
        return velocidade

    def atualizar_posicao(self):
        if self.status == "em viagem":

            # conta mais uma hora de viagem a cada chamada
            self.horas_viagem += 1

            #acelaração gradual
            velocidade_objetivo = self.calcular_velocidade_real()
            if self.velocidade_atual < velocidade_objetivo:
                self.velocidade_atual += 10  # Aceleração de 10 km/h por hora
                if self.velocidade_atual > velocidade_objetivo:
                    self.velocidade_atual = velocidade_objetivo

            self.posicao_km += self.velocidade_atual

            if self.posicao_km >= self.rota.distancia_km:
                self.posicao_km = self.rota.distancia_km
                self.status = "finalizado"
                self.velocidade_atual = 0     
    
    def calcular_receita(self):
        tabela_precos = {
            "minério": 0.10,
            "inter-modal": 0.15,
            "granel": 0.08
        }
        preco = tabela_precos.get(self.tipo_carga, 0.1)

        return self.carga_atual * self.rota.distancia_km * preco
    
    def calcular_custo(self, horas_viagem, atraso):
        custo_combustivel_por_km = 8
  
    # custo aumenta com peso
        fator_peso = 1 + (self.carga_atual / self.capacidade) * 0.5

        custo_fixo_hora = 500
        penalidade_atraso = atraso * 1000

        custo_combustivel = self.rota.distancia_km * custo_combustivel_por_km * fator_peso
        custo_operacional = horas_viagem * custo_fixo_hora

        return custo_combustivel + custo_operacional + penalidade_atraso
    
    def calcular_lucrol(self, receita, custo):
        return receita - custo