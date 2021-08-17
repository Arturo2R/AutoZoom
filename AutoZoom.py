''' AutoZoom
For my first semester in the University. An third semester studiying in my home because the quarantine
This code is a work of __Arturo David Rebolledo Rosenstiehl__  
is prohibited all comercial trades with this software
'''
import datetime
import time
import webbrowser


class Materias:
    def __init__(self, day, horas, profesor, materia, id_reunion):
        self.d = day
        self.h = horas
        self.p = profesor
        self.m = materia
        self.i = id_reunion
        


    def run(self, index):#Ejecutador🗡
        print('ya papito')
        id = str(self.l[index])
        webbrowser.open(f"https://uninorte.zoom.us/j/{id}?uname=Arturo+David+Rebolledo+Rosenstiehl#success", new=0, autoraise=True)#Abre el link de zoom en el navegador
        ok = True
        # print( f'Comenzando clase de {self.m} con il professeur {self.p}')
        time.sleep(3200)
        start()

#----------------------------------------------------Horario De Las Materias -------------------------------------------------#

Competencias_Comunicativas_1 = Materias([1,2], ['08:28_AM', '10:28_AM'], 'Aná Maria Perex Cedeño', 'Competencias Comunicativas I', [89207924504, 89947297325])
Introduccion_Economia = Materias([2,4], ['07:28_AM', '07:28_AM'], 'Jana Schmutzler De Uribe', 'Introducción A la Economía', [85766561053, 89898727252])
Calculo_1 = Materias([2,4], ['12:27_PM', '02:28_PM'], 'German E Jimenez Blanco', 'Calculo 1', [83760728826, 83760728826])
Ingles_8 = Materias([3,4,5], ['04:28_PM', '04:28_PM', '04:28_PM'], 'Por designar', 'Inglés VII', [88024604860, 82184968943, 82700208528])
Literatura_Hispanica = Materias([3], ['09:28_AM'], 'Ernesto Camacho Ocampo', 'Literatura Hispanica', [81275564581])
Proyecto_Vida = Materias([5], ['10:28_AM'], 'Elkin Cabrera Vergara', 'Taller Universitario - Proyecto de Vida', [81275564581])

Todas_las_Clases = [Competencias_Comunicativas_1, Introduccion_Economia, Calculo_1, Ingles_8, Literatura_Hispanica]

#----------------------------------------------------Horario De Las Materias -------------------------------------------------#


#Horario de las Materias
def start():
    today = datetime.datetime.now()
    weekday = int(today.strftime('%w'))
    while weekday > 0 and weekday< 6:
        weekday = int(today.strftime('%w'))
        
        # iterate trough Todas_Las_Clases and if a weekday and hour is correct,  run the method run

    # make a for trough todas_las_clases
        for i in Todas_las_Clases:
            print(weekday)
            if weekday == 2 and '12:29_PM' == today.strftime('%H:%M_%p'):
                i.run(0)
            if len(i.d) == 2:
                if weekday == i.d[1] and i.h[1] == today.strftime('%H:%M_%p'):
                    i.run(1)
            if len(i.d) == 3: 
                if weekday == i.d[2] and i.h[2] == today.strftime('%H:%M_%p'):
                    i.run(2)
        print('un ciclo')
        time.sleep(40)

    if weekday == 0 or weekday == 6:
            time.sleep(32000)
            start()
start()
