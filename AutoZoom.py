''' AutoZoom
For my first semester in the University. An third semester studiying in my home because the quarantine
This code is a work of __Arturo David Rebolledo Rosenstiehl__  
is prohibited all comercial trades with this software
'''
import datetime
import time
import webbrowser

from plyer import notification


class Materias:
    def __init__(self, day, horas, profesor, materia, id_reunion):
        self.d = day
        self.h = horas
        self.p = profesor
        self.m = materia
        self.i = id_reunion

    def run(self, index):#Ejecutador
        id = str(self.i[index])
        notification.notify(
            title='Reunion',
            message=f'En 2 minutos empezara {self.m} con {self.p} a las {self.h[index]}',
            app_name='AutoZoom3',
            app_icon='favicon.ico',
            timeout=10,
        )
        time.sleep(120)
        webbrowser.open(f"https://uninorte.zoom.us/j/{id}?uname=Arturo+David+Rebolledo+Rosenstiehl#success", new=0, autoraise=True)#Abre el link de zoom en el navegador
        time.sleep(3400)
        start()

#----------------------------------------------------Horario De Las Materias -------------------------------------------------#

Competencias_Comunicativas_1 = Materias([1,2], ['08:28_AM', '10:28_AM'], 'Aná Maria Perez Cedeño', 'Competencias Comunicativas I', [89207924504, 89947297325])
Introduccion_Economia = Materias([2,4], ['07:28_AM', '07:28_AM'], 'Jana Schmutzler De Uribe', 'Introducción A la Economía', [85766561053, 89898727252])
Calculo_1 = Materias([2,4], ['14:28_PM', '14:28_PM'], 'German E Jimenez Blanco', 'Calculo 1', [83760728826, 83760728826])
salsa = Materias([2], ['16:28_PM'], 'Linda Galé Coronado', 'Salsa', [84482519185])
Ingles_8 = Materias([3,4,5], ['16:28_PM', '16:28_PM', '17:28_PM'], 'Armando Eeros Rivaldo', 'Inglés VII', [88024604860, 82184968943, 82700208528])
Literatura_Hispanica = Materias([3], ['09:28_AM'], 'Ernesto Camacho Ocampo', 'Literatura Hispanica', [81275564581])
Proyecto_Vida = Materias([5], ['10:28_AM'], 'Elkin Cabrera Vergara', 'Taller Universitario - Proyecto de Vida', [83576078767])

# List Of All Classes
Todas_las_Clases = [Competencias_Comunicativas_1, Introduccion_Economia, Calculo_1, salsa, Ingles_8, Literatura_Hispanica]

#----------------------------------------------------Horario De Las Materias -------------------------------------------------#

notification.notify(
    title='AutoZoom',
    message='El Programa Ha Iniciado',
    app_icon='favicon.ico',
    timeout=4,
    toast=True
)

#Horario de las Materias
def start():
    today = datetime.datetime.now()
    weekday = int(today.strftime('%w'))
    while weekday > 0 and weekday< 6:

        # Get the Hour in "14:20_PM" format
        current = datetime.datetime.now().strftime('%H:%M_%p');
        
        for i in Todas_las_Clases:
            if len(i.d) == 1:
                if weekday == i.d[0] and i.h[0] == current:
                    i.run(0)
            if len(i.d) == 2:
                if i.h[0] == current and i.d[0] == weekday:
                    i.run(0)
                if i.h[1] == current and i.d[1] == weekday:
                    i.run(1)
            if len(i.d) == 3: 
                if i.h[0] == current and i.d[0] == weekday:
                    i.run(0)
                if i.h[1] == current and i.d[1] == weekday:
                    i.run(1)
                if i.h[2] == current and i.d[2] == weekday:
                    i.run(2)
        time.sleep(40)

    if weekday == 0 or weekday == 6:
            time.sleep(32000)
            start()
start()
