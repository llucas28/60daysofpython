import pyautogui
import time 

print("Posicione o mouse na tela e espere 5 segundos...")
time.sleep(2)

print(pyautogui.position())

x, y = 949, 1416
pyautogui.click(x, y)
print(f"Clicou na primeira posição:{x}, {y}")

x, y = 507, 1411
pyautogui.click(x, y)
print(f"Clicou na primeira posição:{x}, {y}")