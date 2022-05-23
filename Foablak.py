from tkinter import *
from tkinter import messagebox
import math

import trapez
import teglalap
import rombusz
import Négyzet
import Kör
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


def körT():
    Kör.terulet()

def körK():
    Kör.kerulet()

>>>>>>> Stashed changes
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

def paralelogrammaT():
    paralelogramma.terulet()

def paralelogrammaK():
    paralelogramma.kerulet()

>>>>>>> Stashed changes
#Főablak
foablak = Tk()
foablak.title("Síkidomok területe és kerülete ")
foablak.minsize(width = 400, height=100)


menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text='Téglalap', underline=0)
menu1.pack(side=LEFT)
teglalapm=Menu(menu1)
teglalapm.add_command(label='Terület', command=teglalapT, underline=0)
teglalapm.add_command(label='Kerület', command=teglalapK, underline=0)
menu1.config(menu=teglalapm)

menu2=Menubutton(menusor, text='Háromszög', underline=0)
menu2.pack(side=LEFT)
háromszög=Menu(menu2)
menu2.config(menu=háromszög)

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
deltoid=Menu(menu5)
menu5.config(menu=deltoid)

menu6=Menubutton(menusor, text='Rombusz', underline=0)
menu6.pack(side=LEFT)
rombuszm=Menu(menu6)
rombuszm.add_command(label='Terület', command=rombuszT, underline=0)
rombuszm.add_command(label='Kerület', command=rombuszK, underline=0)
menu6.config(menu=rombuszm)
>>>>>>> Stashed changes

menu7=Menubutton(menusor, text='Négyzet', underline=0)
menu7.pack(side=LEFT)
négyzet=Menu(menu7)
menu7.config(menu=négyzet)

menu8=Menubutton(menusor, text='Kör', underline=0)
menu8.pack(side=LEFT)
kör=Menu(menu8)
menu8.config(menu=kör)

foablak.mainloop()