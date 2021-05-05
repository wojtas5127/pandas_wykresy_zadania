import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zad 1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx,header=0)
# print(df)
#
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot()
# plt.legend()
# plt.title('Liczba urodzeń w poszczególnych latach')
# plt.show()

# Zad 2
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx,header=0)
# print(df)
#
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# plt.legend()
# plt.xticks(rotation=0)
# plt.title('Liczba urodzeń w poszczególnych latach')
# plt.show()

# Zad 3

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx,header=0)
# print(df)
# grupa = df[(df['Rok']<= 2017)&(df['Rok']>2012)].groupby(['Plec']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot.pie(subplots=True,autopct='%.2f %%',fontsize=20,figsize=(6,6),legend=(0,0))
# plt.legend()
# plt.title('Liczba urodzeń w poszczególnych latach')
# plt.show()

# Zad 4
#
# df = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
# print(df)
# grupa= df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
# print(grupa)
# wykres = grupa.plot.bar()
# plt.legend()
# plt.xticks(rotation=0)
# plt.title('Ilość zamówień poszczególnych sprzedawców')
# plt.show()