import random
import time

class Simulador:
    def __init__(self, trens):
        self.trens = trens
        self.tempo_simulacao = 0

    def rodar(self):
        print("Iniciando simulação...\n")

        while any(trem.status != "finalizado" for trem in self.trens):
            self.tempo_simulacao += 1
            print(f"\n===== Log {self.tempo_simulacao} =====")

            for trem in self.trens:
                if trem.status == "em viagem":
                    #chance de atraso (20%)
                    if random.random() < 0.2:
                        continue

                    trem.atualizar_posicao()

                    print(f"trem {trem.id_trem}")
                    print(f"   posição: {trem.posicao_km:.1f} km")
                    print(f"   status: {trem.status}")
            time.sleep(1)  # Simula o tempo real (1 segundo por hora)
        print("\nSimulação encerrada.")    