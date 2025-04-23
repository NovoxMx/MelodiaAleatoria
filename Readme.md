# 🎹 Generador de Melodías Aleatorias en Python

Este proyecto permite generar melodías musicales aleatorias utilizando una cadena de Markov sobre una escala de 7 o 12 notas. Las melodías se reproducen con sonidos reales de piano (`.wav`), ofreciendo un resultado mucho más armónico que simples pitidos digitales.

---

## 🚀 Características

- Escoge entre **escala diatónica de 7 notas** o **escala cromática de 12 notas**.
- Usa una **matriz de transición probabilística** para generar melodías suaves y coherentes.
- Reproduce sonidos reales grabados desde un piano utilizando `pygame`.
- Escucha tanto el motivo original como una **variación invertida** del mismo.

---

## 📦 Requisitos

- Python 3.x
- [pygame](https://www.pygame.org/) (para reproducir audio)

### Instalar pygame
```bash
pip install pygame
