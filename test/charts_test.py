import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns 

# Cargar la base de datos en un DataFrame
df = pd.read_csv('nba_salaries_&_stats.csv')

# Crear el gráfico de dispersión
plt.figure(figsize=(16, 8))
plt.scatter(df['PTS'], df['Salary'], color='skyblue', alpha=0.5)
plt.xlabel('Puntos')
plt.ylabel('Salario (en millones)')
plt.title('Relación entre Puntos y Salario de los Jugadores de la NBA')
plt.grid(True)  # Agregar cuadrícula al gráfico

# Establecer los límites de los ejes
plt.xlim(0, 35)  # Limitar el eje x de 0 a 100 puntos
plt.ylim(0, 40000000)  # Limitar el eje y de 0 a 40 millones de dólares

# Formatear etiquetas del eje y para mostrar valores enteros
formatter = FuncFormatter(lambda x, _: f'{int(x / 1000000)}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.show()