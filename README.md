# SleepOnKey

SleepOnKey est une petite application Python qui met automatiquement l'écran en veille dès qu'une touche du clavier est pressée.

## Objectif
Créer un utilitaire léger pour économiser l'énergie et sécuriser l'accès à une machine de manière rapide et intuitive.

## Fonctionnalités
- Surveillance du clavier en temps réel
- Mise en veille instantanée au moindre appui sur une touche

## Technologies utilisées
- Python 3
- [keyboard](https://pypi.org/project/keyboard/) pour la détection de touches
- `ctypes` pour l'appel système de mise en veille

## Installation

```bash
pip install keyboard
