import pandas as pd

# Cargar la base de datos en un DataFrame
df = pd.read_csv('nba_2022-23_all_stats_with_salary.csv')

f3 = ['Player Name','Salary','Position','Age','Team','PTS','Total Minutes']

df2 = df[f3]

print(df2)

# df2.to_csv('nba_salaries_&_stats2.csv', index=False)