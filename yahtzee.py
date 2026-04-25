import random

# Clase Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

# Lanzar dados (distribución uniforme)
def lanzar_dados(n=5):
    return [random.randint(1, 6) for _ in range(n)]

# Calcular puntaje simple (suma de dados)
def calcular_puntaje(dados):
    return sum(dados)

# Simular turno
def turno():
    dados = lanzar_dados()

    # Hasta 2 relanzamientos (simulación simple)
    for _ in range(2):
        # Estrategia: relanzar dados menores a 3
        dados = [d if d >= 3 else random.randint(1, 6) for d in dados]

    return dados

# Simular partida
def simular_partida():
    j1 = Jugador("Jugador 1")
    j2 = Jugador("Jugador 2")

    for _ in range(10):  # 10 turnos por jugador
        dados1 = turno()
        dados2 = turno()

        j1.puntaje += calcular_puntaje(dados1)
        j2.puntaje += calcular_puntaje(dados2)

    if j1.puntaje > j2.puntaje:
        return 1
    elif j2.puntaje > j1.puntaje:
        return 2
    else:
        return 0

# Montecarlo
def simulacion_montecarlo(n=1000):
    resultados = {1:0, 2:0, 0:0}

    for _ in range(n):
        ganador = simular_partida()
        resultados[ganador] += 1

    return resultados

# Ejecutar
resultados = simulacion_montecarlo(1000)

print("Resultados:")
print(f"Jugador 1 gana: {resultados[1]} veces")
print(f"Jugador 2 gana: {resultados[2]} veces")
print(f"Empates: {resultados[0]}")
