from tkinter import *
from tkinter import messagebox
import math
import trapez
import teglalap
import rombusz
import Négyzet
import Kör
import haromszog
import deltoid
import paralelogramma

#Névjegy
def nevjegy():
    abl2 = Toplevel(foablak)
    uz2 = Message(abl2, text="Készítette: Dudás Levente\nCsóka András\nBartek Áron", width=300)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()



def négyzetT():
    Négyzet.terulet()

def négyzetK():
    Négyzet.kerulet()

def deltoidT():
    deltoid.terulet()

def deltoidK():
    deltoid.kerulet()

def körT():
    Kör.terulet()

def körK():
    Kör.kerulet()

def paralelogrammaT():
    paralelogramma.terulet()

def paralelogrammaK():
    paralelogramma.kerulet()

def trapezT():
    trapez.terulet()

def trapezK():
    trapez.kerulet()

def teglalapT():
    teglalap.terulet()

def teglalapK():
    teglalap.kerulet()

def rombuszT():
    rombusz.terulet()

def rombuszK():
    rombusz.kerulet()

def haromszogT():
    haromszog.terulet()

def haromszogK():
    haromszog.kerulet()

#Főablak
foablak = Tk()
foablak.title("Síkidomok területe és kerülete ")
foablak.minsize(width = 400, height=100)


menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu = Menubutton(menusor, text="Fájl", underline=0)
menu.pack(side=LEFT)
fajl=Menu(menu)
fajl.add_command(label="Névjegy", command = nevjegy, underline=0)
fajl.add_command(label="Kilépés", command=foablak.destroy, underline=0)
menu.config(menu = fajl)

menu1=Menubutton(menusor, text='Téglalap', underline=0)
menu1.pack(side=LEFT)
teglalapm=Menu(menu1)
teglalapm.add_command(label='Terület', command=teglalapT, underline=0)
teglalapm.add_command(label='Kerület', command=teglalapK, underline=0)
menu1.config(menu=teglalapm)

menu2=Menubutton(menusor, text='Háromszög', underline=0)
menu2.pack(side=LEFT)
haromszogm=Menu(menu2)
haromszogm.add_command(label="Kerület", command = haromszogK, underline=0)
haromszogm.add_command(label="Terület", command = haromszogT, underline=0)
menu2.config(menu=haromszogm)

menu3=Menubutton(menusor, text='Trapéz', underline=0)
menu3.pack(side=LEFT)
trapezm=Menu(menu3)
trapezm.add_command(label='Terület', command=trapezT, underline=0)
trapezm.add_command(label='Kerület', command=trapezK, underline=0)
menu3.config(menu=trapezm)

menu4=Menubutton(menusor, text='Paraleleogramma', underline=0)
menu4.pack(side=LEFT)
paralelogrammam=Menu(menu4)
paralelogrammam.add_command(label='Terület', command=paralelogrammaT, underline=0)
paralelogrammam.add_command(label='Kerület', command=paralelogrammaK, underline=0)
menu4.config(menu=paralelogrammam)

menu5=Menubutton(menusor, text='Deltoid', underline=0)
menu5.pack(side=LEFT)
deltoidm=Menu(menu5)
deltoidm.add_command(label='Terület', command=deltoidT, underline=0)
deltoidm.add_command(label='Kerület', command=deltoidK, underline=0)
menu5.config(menu=deltoidm)


menu6=Menubutton(menusor, text='Rombusz', underline=0)
menu6.pack(side=LEFT)
rombuszm=Menu(menu6)
rombuszm.add_command(label='Terület', command=rombuszT, underline=0)
rombuszm.add_command(label='Kerület', command=rombuszK, underline=0)
menu6.config(menu=rombuszm)

menu7=Menubutton(menusor, text="Négyzet", underline=0)
menu7.pack(side=LEFT)
négyzet=Menu(menu7)
négyzet.add_command(label="Kerület", command = négyzetK, underline=0)
négyzet.add_command(label="Terület", command = négyzetT, underline=0)
menu7.config(menu=négyzet)

menu8=Menubutton(menusor, text='Kör', underline=0)
menu8.pack(side=LEFT)
kör=Menu(menu8)
kör.add_command(label="Kerület", command = körK, underline=0)
kör.add_command(label="Terület", command = körT, underline=0)
menu8.config(menu=kör)

foablak.mainloop()