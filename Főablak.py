from tkinter import *
from tkinter import messagebox
import math

#Főablak
foablak = Tk()
foablak.title("Síkidomok területe és kerülete ")
foablak.minsize(width = 400, height=100)

def terület():
    
    def szamit():
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        felszin=a*b if a and b !=0 else 'Hiba, az egyik adat 0!'
        mezo3.delete(0,END)
        mezo3.insert(0, str(felszin))
    
    abl3=Toplevel(foablak)
    abl3.title('A téglalap területe')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=5, column=2, sticky=W)
    gomb2=Button(abl3, text='Kilép', command=abl3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    abl3.mainloop()

def kerület():
    
    def szamit():
        a=eval(mezo1.get()) 
        b=eval(mezo2.get())
        terfogat=2*(a+b) if a and b !=0 else 'Hiba, az egyik adat 0!'
        mezo3.delete(0,END)
        mezo3.insert(0,str(terfogat))

    abl3=Toplevel(foablak)
    abl3.title('A téglalap kerülete')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=5, column=2, sticky=W)
    gomb2=Button(abl3, text='Kilép', command=abl3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    abl3.mainloop()


menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)


menu1=Menubutton(menusor, text='Téglalap', underline=0)
menu1.pack(side=LEFT)
teglalap=Menu(menu1)
teglalap.add_command(label='Terület', command=terület, underline=0)
teglalap.add_command(label='Kerület', command=kerület, underline=0)
menu1.config(menu=teglalap)

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
