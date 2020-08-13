'''Zoom In 
For Ariano students in eleven grade
This code is a work of __Arturo David Rebolledo Rosenstiehl__  
is prohibited all comercial trades with this software
Soy La Monda'''
import datetime
import time
import webbrowser

print('Iniciando App...')
time.sleep(2)

def espera(a):
    print( f"esperando siguiente clase. {a}")

futura = 0

class Clases:
    def __init__(self, day, hora, profesor, materia, links):
        self.d = day
        self.h = hora
        self.p = profesor
        self.m = materia
        self.l = links
    def run(self):
        webbrowser.open(self.l, new=0, autoraise=True)
        ok = True
        print( f'Comenzando clase de {self.m} con il professeur {self.p}')
        futura += 1
        next(futura)
        time.sleep(60)
        start()
#----------------------------------------------------Horario De Las Materias -------------------------------------------------#
#Lunes
matematicas1 = Clases(1, '07:28_AM', 'Angelly', 'Matematicas', 'https://us04web.zoom.us/j/5628790956?pwd=eDd3ZDFSODR0VnJrVzRFbEIzQ3h5QT09')
fisica3 = Clases(1, '08:53_AM', 'Pajon', 'Fisica', 'https://us04web.zoom.us/j/5609210902?pwd=eTA3MzQrZlNwZzVBblJ3SURlL3B6UT09') 
comprension_lectora = Clases(1, '9:53_AM', 'Elis', 'Español', 'https://us04web.zoom.us/j/6746001313?pwd=dmJGSDc2UjZ1QUM5czZ5MHYyUHB0Zz09')
ingles1 = Clases(1, '10:33_AM', 'Jean Carlos', 'Ingles', 'https://us04web.zoom.us/j/9181948143?pwd=SThwOERFcjNYM01yV3lkNXhKSVU3QT09')
c_sociales1 = Clases(1, '12:38_PM', 'Rodrigo', 'Ciencias Sociales', 'https://us04web.zoom.us/j/3575812939?pwd=dkJjRG43Yk5JYm9JUG81b2Q2aUhIZz09')
#Martes
quimica1 = Clases(2, '07:28_AM', 'Olidys', 'Quimica', 'https://us04web.zoom.us/j/4498293024?pwd=aGNIdVZSTUdsY2JaZFF4ckhCb29YQT09')
musica1 = Clases(2, '08:53_AM', 'Carlos Harnisch', 'Musica', 'https://us04web.zoom.us/j/9927289850?pwd=RkZoK3ZsMks3c1YxdUhNRitPVnRBdz09')
matematicas2 = Clases(2, '09:53_AM', 'Angelly', 'Matematicas', 'https://us04web.zoom.us/j/5628790956?pwd=eDd3ZDFSODR0VnJrVzRFbEIzQ3h5QT09')
religion1 = Clases(2, '01:18_PM', 'Sonia', 'Religion', 'https://us04web.zoom.us/j/6939865538?pwd=OyALFHtiiJM')
#Miercoles
fisica1 = Clases(3, '07:28_AM', 'Pajon', 'Fisica', 'https://us04web.zoom.us/j/5609210902?pwd=eTA3MzQrZlNwZzVBblJ3SURlL3B6UT09')
informatica1 = Clases(3, '10:33', 'Brayan', 'Informatica', 'https://us04web.zoom.us/j/6691112615?pwd=Mk1JNzljVEFFcGRkLzBEVC93bUpBdz09')
estadisticas1 = Clases(3, '11:18_AM', 'Angelly', 'Estadisticas', 'https://us04web.zoom.us/j/5628790956?pwd=eDd3ZDFSODR0VnJrVzRFbEIzQ3h5QT09')
filosofia1 = Clases(3, '01:18_PM', 'Rodrigo', 'Filosofia', 'https://us04web.zoom.us/j/3575812939?pwd=dkJjRG43Yk5JYm9JUG81b2Q2aUhIZz09')
#Jueves
fisica2 = Clases(4, '08:13_AM', 'Pajon', 'Fisica', 'https://us04web.zoom.us/j/5609210902?pwd=eTA3MzQrZlNwZzVBblJ3SURlL3B6UT09')
labo = Clases(4, '08:53_AM', 'Olidys', 'Laboratorio De Quimica', 'https://us04web.zoom.us/j/4498293024?pwd=aGNIdVZSTUdsY2JaZFF4ckhCb29YQT09')
filosofia2 = Clases(4, '10:33_AM', 'Rodrigo', 'Filosofia', 'https://us04web.zoom.us/j/3575812939?pwd=dkJjRG43Yk5JYm9JUG81b2Q2aUhIZz09')
ingles2 = Clases(4, '11:18_AM', 'Jean Carlos', 'Ingles', 'https://us04web.zoom.us/j/9181948143?pwd=SThwOERFcjNYM01yV3lkNXhKSVU3QT09')
español1 = Clases(4, '01:18_PM', 'Elis', 'Español', 'https://us04web.zoom.us/j/6746001313?pwd=dmJGSDc2UjZ1QUM5czZ5MHYyUHB0Zz09')
#Viernes
direccion1 = Clases(5, '07:00_AM', 'Olidys', 'Direccion Grupal', 'https://us04web.zoom.us/j/4498293024?pwd=aGNIdVZSTUdsY2JaZFF4ckhCb29YQT09')
edu = Clases(5, '08:13_AM', 'Adrianis', 'Danza', 'https://us04web.zoom.us/j/9033825814?pwd=aUk3S2pSUldLRzEvN0p6WDVOWUJNZz09')
quimica2 = Clases(5, '09:53_AM', 'Olidys', 'Quimica', 'https://us04web.zoom.us/j/4498293024?pwd=aGNIdVZSTUdsY2JaZFF4ckhCb29YQT09')
ingles3 = Clases(5, '11:38_AM', 'Jean Carlos', 'Ingles', 'https://us04web.zoom.us/j/9181948143?pwd=SThwOERFcjNYM01yV3lkNXhKSVU3QT09')
español2 = Clases(5, '01:18_PM', 'Elis', 'Español', 'https://us04web.zoom.us/j/6746001313?pwd=dmJGSDc2UjZ1QUM5czZ5MHYyUHB0Zz09')
#Pre-Icfes
icfes = Clases(3, '03:00_PM', 'Random', 'Pre-Icfes', 'https://us02web.zoom.us/j/6657149186?pwd=WTM5K1hKUm9TSEc3WmNWT3pYYWU4Zz09#success')
#----------------------------------------------------Horario De Las Materias -------------------------------------------------#
def next(a):
    todas_las_clases = [matematicas1, fisica3, comprension_lectora, ingles1]
    sgtt = todas_las_clases[2]
    print ( f"{sgtt}" )

hoy = datetime.datetime.now()
hoy_es = hoy.strftime('%A')
print(f"Bonito día hoy es {hoy_es}")
def start(sgt_clase):
    today = datetime.datetime.now()
    weekday = int(today.strftime('%w'))
    next(sgt_clase)
    while weekday > 0 and weekday< 6:
        weekday = int(today.strftime('%w'))
        while weekday == 1: # Dia Lunes
            current = time.strftime('%I:%M_%p')
            time.sleep(5)
            espera(current, weekday)
            if matematicas1.h == current:
                matematicas1.run()
            elif fisica3.h == current:
                fisica3.run()
            elif comprension_lectora.h == current:
                comprension_lectora.run()
            elif ingles1.h == current:
                ingles1.run()
            elif c_sociales1.h == current:
                c_sociales1.run()                
        while weekday == 2: # Dia Martes
            current = time.strftime('%I:%M_%p')
            time.sleep(5)
            espera(current, weekday)
            if quimica1.h == current:
                quimica1.run()
            elif musica1.h == current:
                musica1.run()
            elif matematicas2.h == current:
                matematicas2.run()
            elif religion1.h == current:
                religion1.run()               
        while weekday == 3: # Dia Miercoles
            current = time.strftime('%I:%M_%p')
            time.sleep(5)
            espera(current)
            if fisica1.h == current:
                fisica1.run()
            elif informatica1.h == current:
                informatica1.run()
            elif matematicas2.h == current:
                matematicas2.run()
            elif filosofia1.h == current:
                filosofia1.run()      
            elif icfes.h == current:
                icfes.run()         
        while weekday == 4: # Dia Jueves
            current = time.strftime('%I:%M_%p')
            time.sleep(5)
            espera(current)
            if fisica2.h == current:
                fisica2.run()
            elif labo.h == current:
                labo.run()
            elif filosofia2.h == current:
                filosofia2.run()
            elif ingles2.h == current:
                ingles2.run()
            elif español1.h == current:
                español1.run()
            elif icfes.h == current:
                icfes.run()             
        while weekday == 5: # Dia Viernes
            current = time.strftime('%I:%M_%p')
            time.sleep(5)
            espera(current)
            if direccion1.h == current:
                direccion1.run()
            elif edu.h == current:
                edu.run()
            elif quimica2.h == current:
                quimica2.run()
            elif ingles3 == current:
                ingles3.run()
            elif español2.h == current:
                español2.run()
    if weekday == 0 or weekday == 6:
            time.sleep(32000)
            start()
start(futura)