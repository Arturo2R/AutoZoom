''' AutoZoom
For my first semester in the University. An third semester studiying in my home because the quarantine
This code is a work of __Arturo David Rebolledo Rosenstiehl__  
is prohibited all comercial trades with this software
'''
import datetime
import time
import webbrowser
import random

#Saludo Inicial del día
print('Iniciando App...')
time.sleep(2)
lindo_dia = ["Bonito día","Hermoso día que es hoy","Que hermosa mañana","Es inefable lo bello que es este día",
            "Que Belleza de día, hay que aprovechar cada segundo de él", "Que hermoso día que Dios nos ha regalado, para que hobremos de magna manera",
            "Que Buen día hace hoy", "Cada nuevo día es una nueva oportunidad para hacer félices a otros"]

que_dia = random.choice(lindo_dia)
hoy = datetime.datetime.now()
hoy_es = hoy.strftime('%A')
print(f'{que_dia}, hoy es {hoy_es}')

def espera(a): #a:current b:weekday
    time.sleep(20)
    print( f'esperando siguiente clase. {a}')
#Base De datos de las Materias
class Materias:
    def __init__(self, day, horas, profesor, materia, id_reunion):
        self.d = [1,2] #day
        self.h = ['04:28_PM', '04:28_PM']#horas
        self.p = profesor
        self.m = materia
        self.i = ['80853948', '4383945']#id_reunion
        
        # iterate trough days and create this object {dia: 1, hora: horas[1], link} per item
        # for i, j in (len(self.d), self.d):
        #     self.clases.append({'dia': self.d[j], 'hora': self.h[i], 'link': self.l[i]})

        for i in self.d:
            print(i)
                    # self.clases.append({'dia': self.d[j], 'hora': self.h[i], 'link': self.l[i]})



    def run(self):#Ejecutador🗡
        webbrowser.open(self.l, new=0, autoraise=True)#Abre el link de zoom en el navegador
        ok = True
        print( f'Comenzando clase de {self.m} con il professeur {self.p}')
        time.sleep(60)
        start()

#----------------------------------------------------Horario De Las Materias -------------------------------------------------#

Competencias_Comunicativas_1 = Materias([1,2], ['08:28_AM', '10:28_AM'], 'Aná Maria Perex Cedeño', ['89207924504', '89947297325'])
Introduccion_Economia = Materias([2,4], ['07:28_AM', '07:28_AM'], 'Jana Schmutzler De Uribe', 'Introducción A la Economía', ['85766561053', '89898727252'])
Calculo_1 = Materias([2,4], ['02:28_PM', '02:28_PM'], 'German E Jimenez Blanco', 'Calculo 1', ['83760728826', '83760728826'])
Ingles_8 = Materias([3,4,5], ['04:28_PM', '04:28_PM', '04:28_PM'], 'Por designar', 'Inglés VII', ['88024604860', '82184968943', '82700208528'])
Literatura_Hispanica = Materias([3], ['09:28_AM'], 'Ernesto Camacho Ocampo', 'Literatura Hispanica', ['81275564581'])
# Proyecto_Vida = Materias([5], ['10:28_AM'], 'Elkin Cabrera Vergara', 'Taller Universitario - Proyecto de Vida', ['81275564581'])

Todas_las_Clases = [Competencias_Comunicativas_1, Introduccion_Economia, Calculo_1, Ingles_8, Literatura_Hispanica]

#----------------------------------------------------Horario De Las Materias -------------------------------------------------#


#Horario de las Materias
def start():
    today = datetime.datetime.now()
    weekday = int(today.strftime('%w'))
    while weekday > 0 and weekday< 6:
        weekday = int(today.strftime('%w'))
        
        # iterate trough Todas_Las_Clases and if a weekday and hour is correct,  run the method run




    if weekday == 0 or weekday == 6:
            time.sleep(32000)
            start()
start()
