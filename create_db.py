# RUN FROM SHELL

from odb.models import Home
import random
from functools import reduce

# Всякие используемые циферки

norm_temp = {1: 891, 2: 865, 3: 755, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 480, 11: 604, 12: 947}
norm_el = {1: 408, 2: 456, 3: 264, 4: 240, 5: 224, 6: 97, 7: 72, 8: 120, 9: 280, 10: 336, 11: 372, 12: 408}
norm_aqua_hot = {1: 3.5, 2: 3.2, 3: 3, 4: 3, 5: 2.5, 6: 3, 7: 2.6, 8: 2, 9: 2.3, 10: 3, 11: 3.3, 12: 3.4}
norm_aqua_cold = {1: 1.5, 2: 1.8, 3: 2, 4: 2, 5: 2.5, 6: 3, 7: 5.4, 8: 3, 9: 3.7, 10: 2, 11: 1.7, 12: 2.6}

coef_temp = {1: 90, 2: 70, 3: 65, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 40, 11: 60, 12: 90}
coef_aqua = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5, 5: 0.5, 6: 0.5, 7: 0.5, 8: 0.5, 9: 0.5, 10: 0.5, 11: 0.5, 12: 0.5, }
coef_el = {1: 40, 2: 45, 3: 25, 4: 25, 5: 25, 6: 25, 7: 20, 8: 25, 9: 28, 10: 35, 11: 35, 12: 40}

check_coef_temp = {1: 100, 2: 100, 3: 100, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 100, 11: 100, 12: 100}
check_coef_aqua = {1: 0.75, 2: 0.75, 3: 0.75, 4: 0.75, 5: 0.75, 6: 0.75, 7: 0.75, 8: 0.75, 9: 0.75, 10: 0.75, 11: 0.75,
                   12: 0.75}
check_coef_el = {1: 75, 2: 75, 3: 75, 4: 75, 5: 75, 6: 75, 7: 75, 8: 75, 9: 75, 10: 75, 11: 75, 12: 75}

# Создание БД

for i in range(10000):
    d = random.randint(1, 12)
    ah = round(random.uniform(norm_aqua_hot[d] - coef_aqua[d], norm_aqua_hot[d] + coef_aqua[d]), 2)
    ac = round(random.uniform(norm_aqua_cold[d] - coef_aqua[d], norm_aqua_cold[d] + coef_aqua[d]), 2)
    el = random.randint(norm_el[d] - coef_el[d], norm_el[d] + coef_el[d])
    temp = random.randint(norm_temp[d] - coef_temp[d], norm_temp[d] + coef_temp[d])
    Home.objects.create(city=random.randint(1, 3), street=random.randint(1, 5), house=random.randint(1, 15),
                        flat=random.randint(1, 20), date=d, year=random.randint(2000, 2021), temp=temp, aqua_cold=ac,
                        aqua_hot=ah, el=el)

# Добавление аномальных данных

for i in range(500):
    min_or_max = random.randint(0, 1)
    rand_parameter = random.randint(5, 8)
    rand_id = random.randint(0, 10000)
    d = Home.objects.get(id=rand_id).date
    if min_or_max == 0:
        if rand_parameter == 5:
            Home.objects.filter(id=rand_id).update(
                aqua_hot=round(random.uniform(0, norm_aqua_hot[d] - coef_aqua[d]), 2))
        elif rand_parameter == 6:
            Home.objects.filter(id=rand_id).update(aqua_cold=round(
                random.uniform(0, norm_aqua_cold[d] - coef_aqua[d]), 2))
        elif rand_parameter == 7:
            Home.objects.filter(id=rand_id).update(el=random.randint(0, round(norm_el[d] - coef_el[d])))
        elif rand_parameter == 8:
            Home.objects.filter(id=rand_id).update(temp=random.randint(0, round(norm_temp[d] - coef_temp[d])))
    elif min_or_max == 1:
        if rand_parameter == 5:
            Home.objects.filter(id=rand_id).update(
                aqua_hot=round(random.uniform(norm_aqua_hot[d] + coef_aqua[d], 10), 2))
        elif rand_parameter == 6:
            Home.objects.filter(id=rand_id).update(
                aqua_cold=round(random.uniform(norm_aqua_cold[d] + coef_aqua[d], 10), 2))
        elif rand_parameter == 7:
            Home.objects.filter(id=rand_id).update(el=random.randint(round(norm_el[d] + coef_el[d]), 1500))
        elif rand_parameter == 8:
            Home.objects.filter(id=rand_id).update(temp=random.randint(round(norm_temp[d] + coef_temp[d]), 1500))

# Нахождение аномалий

anomalies = []
m_ah = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
m_ac = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
m_el = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
m_temp = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
for i in range(1, 10001):
    d = Home.objects.get(id=i).date
    m_ah[d].append(Home.objects.get(id=i).aqua_hot)
    m_ac[d].append(Home.objects.get(id=i).aqua_cold)
    m_el[d].append(Home.objects.get(id=i).el)
    m_temp[d].append(Home.objects.get(id=i).temp)

# Нахождение аномалий через среднее арифметическое со средним отклонением

arith_ah = {}
arith_ac = {}
arith_el = {}
arith_temp = {}

for i in range(1, 13):
    arith_ah[i] = sum(m_ah[i]) / len(m_ah[i])
    arith_ac[i] = sum(m_ac[i]) / len(m_ac[i])
    arith_el[i] = sum(m_el[i]) / len(m_el[i])
    arith_temp[i] = sum(m_temp[i]) / len(m_temp[i])

dev_ah = {}
dev_ac = {}
dev_el = {}
dev_temp = {}

for i in range(1, 13):
    m_ah[i] = [abs(x - arith_ah[i]) for x in m_ah[i]]
    m_ac[i] = [abs(x - arith_ac[i]) for x in m_ac[i]]
    m_el[i] = [abs(x - arith_el[i]) for x in m_el[i]]
    m_temp[i] = [abs(x - arith_temp[i]) for x in m_temp[i]]

for i in range(1, 13):
    dev_ah[i] = sum(m_ah[i]) / len(m_ah[i])
    dev_ac[i] = sum(m_ac[i]) / len(m_ac[i])
    dev_el[i] = sum(m_el[i]) / len(m_el[i])
    dev_temp[i] = sum(m_temp[i]) / len(m_temp[i])

for i in range(4, 10):
    arith_temp[i] = 0
    dev_temp[i] = 0

for i in range(1, 10001):
    d = Home.objects.get(id=i).date
    ah = Home.objects.get(id=i).aqua_hot
    ac = Home.objects.get(id=i).aqua_cold
    el = Home.objects.get(id=i).el
    temp = Home.objects.get(id=i).temp
    if ah > arith_ah[d] + dev_ah[d]:
        anomalies.append({"id": i, "anomaly": "Hot Water too much"})
    elif ah < arith_ah[d] - dev_ah[d]:
        anomalies.append({"id": i, "anomaly": "Hot Water too low"})
    if ac > arith_ac[d] + dev_ac[d]:
        anomalies.append({"id": i, "anomaly": "Cold Water too much"})
    elif ac < arith_ac[d] - dev_ac[d]:
        anomalies.append({"id": i, "anomaly": "Cold Water too low"})
    if el > arith_el[d] + dev_el[d]:
        anomalies.append({"id": i, "anomaly": "Electric too much"})
    elif el < arith_el[d] - dev_el[d]:
        anomalies.append({"id": i, "anomaly": "Electric too low"})
    if temp > arith_temp[d] + dev_temp[d]:
        anomalies.append({"id": i, "anomaly": "Temperature too much"})
    elif temp < arith_temp[d] - dev_temp[d]:
        anomalies.append({"id": i, "anomaly": "Temperature too low"})

# Нахождение аномалий через среднее геометрическое (слишком большие числа, питон отказывается считать)
# geom_ah = {}
# geom_ac = {}
# geom_el = {}
# geom_temp = {}
# for i in range(1, 13):
#     geom_ah[i] = round(reduce((lambda x, y: x * y), m_ah[i]) ** round(1 / len(m_ah[i]), 5), 4)
#     geom_ac[i] = round(reduce((lambda x, y: x * y), m_ac[i]) ** round(1 / len(m_ac[i]), 5), 4)
#     geom_el[i] = round(reduce((lambda x, y: x * y), m_el[i]) ** round(1 / len(m_el[i]), 5), 4)
#     geom_temp[i] = round(reduce((lambda x, y: x * y), m_temp[i]) ** round(1 / len(m_temp[i]), 5), 4)
#
# for i in range(4, 10):
#     arith_temp[i] = 0
#
# for i in range(1, 10001):
#     d = Home.objects.get(id=i).date
#     ah = Home.objects.get(id=i).aqua_hot
#     ac = Home.objects.get(id=i).aqua_cold
#     el = Home.objects.get(id=i).el
#     temp = Home.objects.get(id=i).temp
#     if ah > geom_ah[d] + coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Hot Water too much"})
#     elif ah < geom_ah[d] - coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Hot Water too low"})
#     if ac > geom_ac[d] + coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Cold Water too much"})
#     elif ac < geom_ac[d] - coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Cold Water too low"})
#     if el > geom_el[d] + coef_el[d]:
#         anomalies.append({"id": i, "anomaly": "Electric too much"})
#     elif el < geom_el[d] - coef_el[d]:
#         anomalies.append({"id": i, "anomaly": "Electric too low"})
#     if temp > geom_temp[d] + coef_temp[d]:
#         anomalies.append({"id": i, "anomaly": "Temperature too much"})
#     elif temp < geom_temp[d] - coef_temp[d]:
#         anomalies.append({"id": i, "anomaly": "Temperature too low"})

# Нахождение аномалий через средрее арифметическое (1431 аномалия из 500 по стандартным данным)
# arith_ah = {}
# arith_ac = {}
# arith_el = {}
# arith_temp = {}
# for i in range(1, 13):
#     arith_ah[i] = sum(m_ah[i]) / len(m_ah[i])
#     arith_ac[i] = sum(m_ac[i]) / len(m_ac[i])
#     arith_el[i] = sum(m_el[i]) / len(m_el[i])
#     arith_temp[i] = sum(m_temp[i]) / len(m_temp[i])
#
# for i in range(4, 10):
#     arith_temp[i] = 0
#
# for i in range(1, 10001):
#     d = Home.objects.get(id=i).date
#     ah = Home.objects.get(id=i).aqua_hot
#     ac = Home.objects.get(id=i).aqua_cold
#     el = Home.objects.get(id=i).el
#     temp = Home.objects.get(id=i).temp
#     if ah > arith_ah[d] + coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Hot Water too much"})
#     elif ah < arith_ah[d] - coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Hot Water too low"})
#     if ac > arith_ac[d] + coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Cold Water too much"})
#     elif ac < arith_ac[d] - coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Cold Water too low"})
#     if el > arith_el[d] + coef_el[d]:
#         anomalies.append({"id": i, "anomaly": "Electric too much"})
#     elif el < arith_el[d] - coef_el[d]:
#         anomalies.append({"id": i, "anomaly": "Electric too low"})
#     if temp > arith_temp[d] + coef_temp[d]:
#         anomalies.append({"id": i, "anomaly": "Temperature too much"})
#     elif temp < arith_temp[d] - coef_temp[d]:
#         anomalies.append({"id": i, "anomaly": "Temperature too low"})

# Нахождение аномалий через медиану (3000 с небольшим аномалий из 500 созданных по очень сильно повышенным критериям)
# for i in range(1, 13):
#     sorted(m_ah[i])
#     sorted(m_ac[i])
#     sorted(m_temp[i])
#     sorted(m_el[i])
#
# median_ah = {}
# median_ac = {}
# median_temp = {}
# median_el = {}
#
# if n % 2 == 0:
#     for i in range(1, 13):
#         median_ah[i] = (m_ah[i][len(m_ah[i]) // 2] + m_ah[i][len(m_ah[i]) // 2 + 1]) // 2
#         median_ac[i] = (m_ac[i][len(m_ac[i]) // 2] + m_ac[i][len(m_ac[i]) // 2 + 1]) // 2
#         median_el[i] = (m_el[i][len(m_el[i]) // 2] + m_el[i][len(m_el[i]) // 2 + 1]) // 2
#         median_temp[i] = (m_temp[i][len(m_temp[i]) // 2] + m_temp[i][len(m_temp[i]) // 2 + 1]) // 2
# else:
#     for i in range(1, 13):
#         median_ah[i] = m_ah[i][len(m_ah[i]) // 2 + 1]
#         median_ac[i] = m_ac[i][len(m_ac[i]) // 2 + 1]
#         median_el[i] = m_el[i][len(m_el[i]) // 2 + 1]
#         median_temp[i] = m_temp[i][len(m_temp[i]) // 2 + 1]
#
# for i in range(1, 10000):
#     d = Home.objects.get(id=i).date
#     ah = Home.objects.get(id=i).aqua_hot
#     ac = Home.objects.get(id=i).aqua_cold
#     el = Home.objects.get(id=i).el
#     temp = Home.objects.get(id=i).temp
#     if ah > median_ah[d] + check_coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Hot Water too much"})
#     elif ah < median_ah[d] - check_coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Hot Water too low"})
#     if ac > median_ac[d] + check_coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Cold Water too much"})
#     elif ac < median_ac[d] - check_coef_aqua[d]:
#         anomalies.append({"id": i, "anomaly": "Cold Water too low"})
#     if el > median_el[d] + check_coef_el[d]:
#         anomalies.append({"id": i, "anomaly": "Electric too much"})
#     elif el < median_el[d] - check_coef_el[d]:
#         anomalies.append({"id": i, "anomaly": "Electric too low"})
#     if temp > median_temp[d] + check_coef_temp[d]:
#         anomalies.append({"id": i, "anomaly": "Temperature too much"})
#     elif temp < median_temp[d] - check_coef_temp[d]:
#         anomalies.append({"id": i, "anomaly": "Temperature too low"})

# Прогнозирование

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import homes.csv

# import sqlite3 бесполезная шняга
#
# conn = sqlite3.connect(r'C:\Users\G119\PycharmProjects\DHU\hello\db.sqlite3')
# cur = conn.cursor()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS homes(
#    homeid INT PRIMARY KEY,
#    city INT,
#    house INT,
#    flat INT,
#    date INT,
#    year INT,
#    aquahot INT,
#    aquacold INT,
#    el INT,
#    temp INT);
# """)
# conn.commit()
#
# for i in range(1, 10000):
#     home = Home.objects.get(id=i)
#     home_c = (
#         home.id, home.city, home.house, home.flat, home.date, home.year, home.aqua_hot, home.aqua_cold, home.el,
#         home.temp)
#     cur.execute("INSERT INTO homes VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", home_c)
# conn.commit()
#
# cur.execute("""SELECT *
# FROM homes
# WHERE year == '2001';""")
#
# all_2001 = cur.fetchall()

df = pd.read_csv('homes.csv')
