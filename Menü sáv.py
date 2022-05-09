from tkinter import *
from tkinter import messagebox
import math

#Főablak
foablak = Tk()
foablak.title("Síkidomok területe és kerülete ")
foablak.minsize(width = 400, height=100)

menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu1=Menubutton(menusor, text='Téglatest', underline=0)
menu1.pack(side=LEFT)
teglatest=Menu(menu1)

menu1.config(menu=teglatest)
menu2=Menubutton(menusor, text='Háromszög', underline=0)
menu2.pack(side=LEFT)
háromszög=Menu(menu2)

menu2.config(menu=háromszög)
menu3=Menubutton(menusor, text='Trapéz', underline=0)
menu3.pack(side=LEFT)
trapéz=Menu(menu3)
menu3.config(menu=trapéz)

menu4=Menubutton(menusor, text='Paraleleogramma', underline=0)
menu4.pack(side=LEFT)
paralelogramma=Menu(menu4)
menu4.config(menu=paralelogramma)

menu5=Menubutton(menusor, text='Deltoid', underline=0)
menu5.pack(side=LEFT)
deltoid=Menu(menu5)
menu5.config(menu=deltoid)

menu6=Menubutton(menusor, text='Rombusz', underline=0)
menu6.pack(side=LEFT)
rombusz=Menu(menu6)
menu6.config(menu=rombusz)

menu7=Menubutton(menusor, text='Négyzet', underline=0)
menu7.pack(side=LEFT)
négyzet=Menu(menu7)
menu7.config(menu=négyzet)

menu8=Menubutton(menusor, text='Kör', underline=0)
menu8.pack(side=LEFT)
kör=Menu(menu8)
menu8.config(menu=kör)

foablak.mainloop()