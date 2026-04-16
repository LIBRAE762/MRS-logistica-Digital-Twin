from trem import Trem
from rota import Rota
from simulador import Simulador

# Criando rotas
rota1 = Rota("São Paulo", "Rio de Janeiro", 830, tipo_terreno="serra")
rota2 = Rota("Belo Horizonte", "Salvador", 1200, tipo_terreno="plano")

# Criando trens
trem1 = Trem(2497, "minério", 10000, 70)
trem2 = Trem(1420, "inter-modal", 5000, 70)

# Carregando trens
trem1.carregar(8000)
trem2.carregar(5000)

# Iniciando viagens
trem1.iniciar_viagem(rota1)
trem2.iniciar_viagem(rota2)

# rodando simulação
simulador = Simulador([trem1, trem2])
simulador.rodar()

# Resumo final dos trens
print("\n===== Resumo Final dos Trens =====")
for trem in simulador.trens:
	receita = trem.calcular_receita()
	custo = trem.calcular_custo(trem.horas_viagem, trem.atraso_total)
	lucroL = trem.calcular_lucrol(receita, custo)
	print(f"Trem {trem.id_trem} - carga: {trem.carga_atual} t, distancia: {trem.rota.distancia_km} km")
	print(f"  horas viagem: {trem.horas_viagem} h")
	print(f"  receita: R$ {receita:.2f}")
	print(f"  custo estimado: R$ {custo:.2f}")
	print(f"  lucro liquido: R$ {lucroL:.2f}\n")
