import pygame
import time
import random
import numpy as np

pygame.mixer.init()

# Escalas disponibles
escala_7 = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
escala_12 = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si']

# Elegir cantidad de notas (7 o 12)
while True:
    cantidad = input("¿Cuántas notas deseas usar? (7 o 12): ").strip()
    if cantidad in ['7', '12']:
        cantidad = int(cantidad)
        break
    print("Por favor, escribe 7 o 12.")

# Seleccionar escala según elección
notas = escala_7 if cantidad == 7 else escala_12

# Cargar sonidos (Armonicas)
try:
    sonidos = {nota: pygame.mixer.Sound(f"Tonos/{nota}.wav") for nota in notas}
except FileNotFoundError as e:
    print("Error: Asegúrate de tener los archivos .wav para todas las notas seleccionadas.")
    raise e

n = len(notas)
P = np.zeros((n, n))

# Matriz de transición (más probabilidad a notas cercanas)
for i in range(n):
    for j in range(n):
        distancia = abs(i - j)
        if cantidad == 12 and distancia > 6:
            distancia = 12 - distancia  # ciclo circular
        P[i][j] = 1 / (1 + distancia)

# Normalizar filas para que sumen 1
P = P / P.sum(axis=1, keepdims=True)

# Funcion para reproducir sonido
def reproducir_nota(nota):
    sonido = sonidos[nota]
    sonido.play()
    if notas == escala_7:
        time.sleep(0.4) # Tiempo de espera para notas de 7 tonos
    else:
        time.sleep(0.4) # Tiempo de espera para notas de 12 tonos
   

# Generar Ritmo Aleatorio
def generar_motivo(longitud): 
    motivo = []
    estado_actual = random.randint(0, n - 1)
    for _ in range(longitud):
        nota = notas[estado_actual]
        motivo.append(nota)
        estado_actual = np.random.choice(range(n), p=P[estado_actual])
    return motivo

# Funcion para generar melodía con sonido
def generar_melodia_con_sonido(n_repeticiones=4):
    
    # Generar Longitud de motivo en función de la escala elegida
    if notas == escala_7:
        longitud = 6
    else:
        longitud = 8
        
    for _ in range(n_repeticiones):
        motivo = generar_motivo(longitud)
        print("Motivo:", motivo)
        for nota in motivo:
            print(f"Nota: {nota}")
            reproducir_nota(nota)

        motivo_variado = motivo[::-1]
        print("Variación:", motivo_variado)
        for nota in motivo_variado:
            print(f"Nota: {nota}")
            reproducir_nota(nota)

generar_melodia_con_sonido()
