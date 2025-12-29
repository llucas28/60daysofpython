#pip install plotext

import plotext as plt

power_levels = {
    "Goku": 9000,
    "Vegeta": 8500,
    "Frieza": 12000,
    "Piccolo": 6000,
    "Gohan": 7500
}

personagens = list(power_levels.keys())
poder = list(power_levels.values())

plt.title("Níveis dee poder de Dragon Ball Z")

plt.xlabel("Personagens")
plt.ylabel("Níveis de poder")

plt.bar(personagens, poder, label="Nivel de poder")

plt.show()
