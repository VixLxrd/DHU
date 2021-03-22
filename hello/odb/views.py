from django.shortcuts import render
from .models import Home
from django.http import HttpResponse


def index(request):
    homes = Home.objects.all()

    return render(request, 'index.html', {'homes': homes})


def anomalies(request):
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
    return render(request, 'anomalies.html', {'anomalies': anomalies})
