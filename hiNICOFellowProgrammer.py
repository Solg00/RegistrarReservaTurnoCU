# listaNotas = [10]
# dic = {"Nico" : listaNotas,
#        "Caro" : [9],
#        "Diego": [8]}
#
# dic["Nico"].append(9)
# print(dic)

turnosAgrupados = {}
turnos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
for turno in turnos:
    turnosDia = []
    fechaTurno = turno
    fechas = turnosAgrupados.keys()
    if fechaTurno not in fechas:
        turnosAgrupados[fechaTurno] = turnosDia
        turnosAgrupados[fechaTurno].append(turno)
    else:
        turnosAgrupados[fechaTurno].append(turno)

print(turnosAgrupados)
