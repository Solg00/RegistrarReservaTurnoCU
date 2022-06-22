"""HELLO BUDDY! You might use this module to run some tests or leave comments for your fellow Programmers to see"""
from CambioEstadoRT import CambioEstadoRT
from Estado import Estado
from Marca import Marca
from Modelo import Modelo
from RecursoTecnologico import RecursoTecnologico
mod1 = Modelo('Modelo 1')
mod2 = Modelo('modelo2')
mod3 = Modelo('mod 3')
m1 = Marca('Marca1',[mod1,mod3])
m2= Marca('Marca 2', [mod2] )

e1= Estado('Reservado','','',False,True)
e2= Estado('Disponible','','',True,False)

ce1= CambioEstadoRT(e1,'10/10/2021 10:20')
ce2=CambioEstadoRT(e2,'12/12/2021 10:20')
rt =  RecursoTecnologico(21312132,'10/10/2021','','','','',mod1,'',[ce1,ce2],'')
rt2 =  RecursoTecnologico(21312132,'10/10/2021','','','','',mod3,'','','')

print(rt2.miModeloYMarca([m1,m2]))

p = [{'ci':'UTN FRC', 'nro_Inv': 1},{'ci': 'UTN FRBA', 'nro_Inv': 2},{'ci':'UTN FRC', 'nro_Inv': 23131},{'ci':'UTN FRBA', 'nro_Inv': 231312}]


col = {}

for o in p:
    if o.get('ci') in col.keys():
        col[o.get('ci')].append({'nro_Inv': o.get('nro_Inv')})
    else:
        col[ o.get('ci')] = [{'nro_Inv': o.get('nro_Inv')}]

print(col)