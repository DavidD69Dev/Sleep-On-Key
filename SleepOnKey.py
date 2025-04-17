import keyboard
import os
import ctypes

def sleep_windows():
    # Active le mode veille
    ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

def on_key(event):
    print(f"Touche détectée : {event.name}. Mise en veille...")
    sleep_windows()

keyboard.on_press(on_key)

print("L'application est en attente d'une touche...")
keyboard.wait()  # Garde le script en exécution
#cd dv
